"""Colormappy
"""

# standard
import colorsys

# 3rd party
import numpy
from scipy.interpolate import interp1d
from numpy.polynomial import Polynomial
from scipy.signal import savgol_filter
from scipy.ndimage import gaussian_filter1d

from colorspacious import cspace_convert

# local
from colormappy.predicates import is_acceptable_colorspace_3tuple
from colormappy.utils import greyscale_RGB
from colormappy.colortransforms import hls_full_saturation, hls_saturate, \
    hls_desaturate, hls_complementary_color, hls_lighten, hls_darken, \
    Jpapbp_darken, Jpapbp_lighten, Jpapbp_tone, CIELCh_complementary, \
    CIELCh_darken, CIELCh_lighten, Jpapbp_neutral, JCh_desaturate, \
    JCh_saturate, JCh_darken, JCh_lighten

# colormaps are essentially vectored valued functions in a color space and can be defined by the parametric equations:
# x(t), y(t), z(t) where t is the index parameter within the array

class ColorPointIndex(object):
    """A single point within a colormap defined by an index value and three color values in a defined color space.
    Color values may correspond to rgb, XYZ, xyY, J'a'b', ect.
    """
    def __init__(self, idx:float, c0:float, c1:float, c2:float, cspace:str):
        """Constructor method.

        Parameters
        ----------
        idx : float
            Index location of a point within a colormap array
        c0 : float
            Color value in color space (first index, e.g. red value in rgb space)
        c1 : float
            Color value in color space
        c2 : float
            Color value in color space
        cspace : str
            Color space associated with the color values (defined by colorspacious)
        """
        self.idx = idx
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
        # assert cspace is one of the defined colorspacious color spaces or subset, e.g. JCh
        try:
            assert(is_acceptable_colorspace_3tuple(cspace=cspace))
            self.cspace = cspace
        except AssertionError as err:
            print("cspace {} is not an acceptable input colorspace.".format(cspace))
            raise err
        

    # TODO: __repr__
    # better info with f'index: {self.idx}, red: {self.c0}, green: {sel.c1}, blue: {self.c2}'
    def __str__(self):
        s = str(self.idx) + ", "
        s += str(self.c0) + ", "
        s += str(self.c1) + ", "
        s += str(self.c2)
        return s


def create_colormap(points: list, interp_cspace="CAM02-UCS", interp_method="linear") -> numpy.ndarray:
    """Create a colormap via interpolation in interp_cspace color space and output in sRGB1 color space given a list of :class `colormappy.colorpointindex.ColorPointIndex` objects.

    Parameters
    ----------
    points : list
        List of :class `colormappy.colorpointindex.ColorPointIndex` objects
    interp_cspace : str
        Color space in which to do the interpolation; must be one of the defined colorspacious color spaces
    interp_method: str
        Interplolation method used in scipy.interpolate.interp1d `kind` parameter. default='linear'
    
    Returns
    -------
    class `numpy.ndarray` of shape (256,3) in sRGB1 colorspace
    """
    # TODO: verify interp_method is one of the strings accepted by scipy interp1d
    # points must be a list of ColorPointIndex objects; TODO: add try/except block and assert each element of list is of type ColorPointIndex
    # later versions should attempt to convert item to ColorPointIndex object
    # assert cspace is one of the defined colorspacious color spaces or subset, e.g. JCh
    try:
        assert(is_acceptable_colorspace_3tuple(cspace=interp_cspace))
    except AssertionError:
        print("interp_cspace {} is not an acceptable input colorspace. Using CAM02-UCS uniform colorspace".format(interp_cspace))
        interp_cspace = "CAM02-UCS"
    # output is a numpy array of 256 values
    tmp_arr = numpy.zeros(shape=(len(points),3))
    indices = numpy.zeros(shape=(len(points)))
    for n in range(len(points)):
        p = points[n]
        indices[n] = p.idx
        tmp_arr[n,:] = cspace_convert([p.c0, p.c1, p.c2], p.cspace, interp_cspace)
    
    f0 = interp1d(indices, tmp_arr[:,0], kind=interp_method)  # color0  interpolation function in interp_cspace
    f1 = interp1d(indices, tmp_arr[:,1], kind=interp_method)  # color1  interpolation function in interp_cspace
    f2 = interp1d(indices, tmp_arr[:,2], kind=interp_method)  # color2  interpolation function in interp_cspace

    # TODO: may need to extrapolate if first index > 0 or last index < 255
    ind_new = numpy.arange(256)
    out_arr = numpy.zeros(shape=(256,3))
    out_arr[:,0] = f0(ind_new)  # use interpolation function returned by `interp1d`
    out_arr[:,1] = f1(ind_new)  # use interpolation function returned by `interp1d`
    out_arr[:,2] = f2(ind_new)  # use interpolation function returned by `interp1d`
    out_arr = cspace_convert(out_arr, interp_cspace, "sRGB1")
    return numpy.clip(out_arr, 0.0, 1.0)

def shift_colormap(rgb_arr):
    # TODO: add parameter to indicate amount, or quantile, by which to shift; default = 0.5
    # rgb_arr is a numpy array of shape (256,3)
    return numpy.roll(rgb_arr, 128, axis=0)

def reverse_colormap(rgb_arr):
    # rgb_arr is a numpy array of shape (256,3)
    return numpy.flipud(rgb_arr)

# similarity
def self_similarity(rgb_arr):
    arr1 = rgb_arr[:-1, :]
    arr2 = rgb_arr[1:, :]
    return deltaE(arr1, arr2, input_space="sRGB1")

def blend_colormaps(rgb_arr0, rgb_arr1, weights=(0.5,0.5), space="CAM02-UCS"):
    #
    Jpapbp_arr0 = cspace_convert(rgb_arr0, "sRGB1", space)
    Jpapbp_arr1 = cspace_convert(rgb_arr1, "sRGB1", space)
    Jpapbp_blended = (weights[0] * Jpapbp_arr0) + (weights[1] * Jpapbp_arr1)
    tmp = cspace_convert(Jpapbp_blended, space, "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)

def colormap_mix_greyscale(rgb_arr):
    # blend the input colormap with its greyscale representation; lighter colors move towards white 
    # and darker colors move towards black
    gry = greyscale_RGB(color_rgb=rgb_arr)
    return blend_colormaps(rgb_arr0=rgb_arr, rgb_arr1=gry)

# ---
# applying color theory transforms to entire colormap
def colormap_hls_full_saturation(rgb_arr):
    # create natural color, i.e full saturation and neither tinted nor shaded
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    sat_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        sat_arr[n,:] = hls_full_saturation(tmp)
    return sat_arr

def colormap_hls_saturate(rgb_arr, quantile=0.5):
    # increase saturation
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    sat_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        sat_arr[n,:] = hls_saturate(tmp)
    return sat_arr

def colormap_hls_desaturate(rgb_arr, quantile=0.5):
    # decrease saturation, i.e. move towards grey
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = hls_desaturate(tmp)
    return out_arr

def colormap_hls_complementary_color(rgb_arr):
    # return the complementary color
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = hls_complementary_color(tmp)
    return out_arr

def colormap_hls_lighten(rgb_arr, quantile=0.5):
    # tint - mix white
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = hls_lighten(tmp)
    return out_arr

def colormap_hls_darken(rgb_arr, quantile=0.5):
    # shade - mix black
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = hls_darken(tmp)
    return out_arr
    

# shading, tinting, and toning via interpolation with black, white, or grey in uniform color space
def colormaps_Jpapbp_darken(rgb_arr, quantile=0.5):
    # TODO: assert quantile between 0 and 1
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = Jpapbp_darken(tmp)
    return out_arr



def colormap_Jpapbp_lighten(rgb_arr, quantile=0.5):
    # TODO: assert quantile between 0 and 1
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = Jpapbp_lighten(tmp)
    return out_arr

def colormap_Jpapbp_tone(rgb_arr, quantile=0.5):
    # TODO: assert quantile between 0 and 1
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = Jpapbp_tone(tmp)
    return out_arr

def colormap_CIELCh_complementary(rgb_arr):
    #
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = CIELCh_complementary(tmp)
    return out_arr

def colormap_CIELCh_darken(rgb_arr, quantile=0.5):
    # shade - mix black
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = CIELCh_darken(tmp)
    return out_arr
    

def colormap_CIELCh_lighten(rgb_arr, quantile=0.5):
    # shade - mix black
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = CIELCh_lighten(tmp)
    return out_arr

def colormap_Jpapbp_neutral(rgb_arr, quantile=0.5):
    # mix the base rgb with its complementary color
    # TODO: assert quantile between 0 and 1
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = Jpapbp_neutral(tmp)
    return out_arr

# https://colorspacious.readthedocs.io/en/latest/tutorial.html
def colormap_JCh_desaturate(rgb_arr, quantile=0.5):
    # reduce the "C" value (Chroma)
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = JCh_desaturate(tmp)
    return out_arr

def colormap_JCh_saturate(rgb_arr, quantile=0.5):
    # reduce the "C" value (chroma)
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = JCh_saturate(tmp)
    return out_arr

def colormap_JCh_darken(rgb_arr, quantile=0.5):
    # reduce the "J" value (lightness)
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = JCh_darken(tmp)
    return out_arr

def colormap_JCh_lighten(rgb_arr, quantile=0.5):
    # reduce the "J" value (lightness)
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    out_arr = numpy.zeros_like(rgb_arr)
    for n in range(N):
        tmp = (rgb_arr[n,0], rgb_arr[n,1], rgb_arr[n,2])
        out_arr[n,:] = JCh_lighten(tmp)
    return out_arr

def polyfit_smooth(rgb_arr:numpy.ndarray, n_iters=1, polydeg=1) -> numpy.ndarray:
    N = rgb_arr.shape[0]  # assumes rgb_arr is numpy array; if not, convert to numpy.ndarray and assert shape[1] == 3
    xp = numpy.arange(N)
    Jpapbp = cspace_convert(rgb_arr, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace
    Jpapbp_fit = numpy.copy(Jpapbp)
    
    for _ in range(n_iters):
        pJp = Polynomial.fit(xp, Jpapbp[:,0], deg=polydeg)
        pap = Polynomial.fit(xp, Jpapbp[:,1], deg=polydeg)
        pbp = Polynomial.fit(xp, Jpapbp[:,2], deg=polydeg)

        Jpapbp_fit[:,0] = pJp(xp)  # polynomial fit
        Jpapbp_fit[:,1] = pap(xp)  # polynomial fit
        Jpapbp_fit[:,2] = pbp(xp)  # polynomial fit

        # take the average of the original and fitted
        Jpapbp = (0.5 * Jpapbp) + (0.5 * Jpapbp_fit)

    arr = cspace_convert(Jpapbp, "CAM02-UCS", "sRGB1")
    return numpy.clip(arr, 0, 1)

def gaussian_filter1d_smooth(rgb_arr:numpy.ndarray, n_iters=1, sigma=1) -> numpy.ndarray:
    # N = rgb_arr.shape[0]
    Jpapbp = cspace_convert(rgb_arr, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace
    Jpapbp_smooth = numpy.copy(Jpapbp)

    for _ in range(n_iters):
        Jpapbp_smooth[:,0] = gaussian_filter1d(Jpapbp[:,0], sigma=sigma)
        Jpapbp_smooth[:,1] = gaussian_filter1d(Jpapbp[:,1], sigma=sigma)
        Jpapbp_smooth[:,2] = gaussian_filter1d(Jpapbp[:,2], sigma=sigma)

        # take the average of the original and fitted
        Jpapbp = (0.5 * Jpapbp) + (0.5 * Jpapbp_smooth)

    arr = cspace_convert(Jpapbp, "CAM02-UCS", "sRGB1")
    return numpy.clip(arr, 0, 1)

def savgol_filter_smooth(rgb_arr:numpy.ndarray, n_iters=1, window_length=5, polyorder=2) -> numpy.ndarray:
    # N = rgb_arr.shape[0]
    Jpapbp = cspace_convert(rgb_arr, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace
    Jpapbp_smooth = numpy.copy(Jpapbp)

    for _ in range(n_iters):
        Jpapbp_smooth[:,0] = savgol_filter(Jpapbp[:,0], window_length=window_length, polyorder=polyorder)
        Jpapbp_smooth[:,1] = savgol_filter(Jpapbp[:,1], window_length=window_length, polyorder=polyorder)
        Jpapbp_smooth[:,2] = savgol_filter(Jpapbp[:,2], window_length=window_length, polyorder=polyorder)

        # take the average of the original and fitted
        Jpapbp = (0.5 * Jpapbp) + (0.5 * Jpapbp_smooth)

    arr = cspace_convert(Jpapbp, "CAM02-UCS", "sRGB1")
    return numpy.clip(arr, 0, 1)

