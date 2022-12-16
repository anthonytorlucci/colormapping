"""Colormappy
"""

# standard

# 3rd party
import numpy
from scipy.interpolate import interp1d
#import matplotlib.colors

from colorspacious import cspace_convert

# local
from colormappy.predicates import is_acceptable_colorspace_3tuple

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


def create_colormap(points: list, interp_cspace="CAM02-UCS") -> numpy.ndarray:
    """Create a colormap via interpolation in interp_cspace color space and output in sRGB1 color space given a list of :class `colormappy.colorpointindex.ColorPointIndex` objects.

    Parameters
    ----------
    points : list
        List of :class `colormappy.colorpointindex.ColorPointIndex` objects
    interp_cspace : str
        Color space in which to do the interpolation; must be one of the defined colorspacious color spaces
    
    Returns
    -------
    class `numpy.ndarray` of shape (256,3) in sRGB1 colorspace
    """
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
    
    f0 = interp1d(indices, tmp_arr[:,0])  # color0  interpolation function in interp_cspace
    f1 = interp1d(indices, tmp_arr[:,1])  # color1  interpolation function in interp_cspace
    f2 = interp1d(indices, tmp_arr[:,2])  # color2  interpolation function in interp_cspace

    # TODO: may need to extrapolate if first index > 0 or last index < 255
    ind_new = numpy.arange(256)
    out_arr = numpy.zeros(shape=(256,3))
    out_arr[:,0] = f0(ind_new)  # use interpolation function returned by `interp1d`
    out_arr[:,1] = f1(ind_new)  # use interpolation function returned by `interp1d`
    out_arr[:,2] = f2(ind_new)  # use interpolation function returned by `interp1d`
    out_arr = cspace_convert(out_arr, interp_cspace, "sRGB1")
    return numpy.clip(out_arr, 0.0, 1.0)



