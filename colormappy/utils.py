"""utility functions
"""

# standard library

# 3rd party
import numpy
import matplotlib.cm
import matplotlib.colors

from colorspacious import cspace_convert

# local

# utility functions for working with colormaps
def list_of_tuples_to_array(rgb_list_of_tuples:list) -> numpy.ndarray:
    """convert a list of tuples to a numpy array.

    :param rgb_list_of_tuples: list of tuples each with 3 float values.
    :type rgb_list_of_tuples: list
    :return: array with shape (n,3) where n = len(rgb_list_of_tuples)
    :rtype: class `numpy.ndarray`
    """
    # convert a list of (r,g,b) tuples to numpy array
    # TODO: assert each element in array is a 3-element iterable of floating point values
    n = len(rgb_list_of_tuples)
    arr = numpy.zeros(shape=(n,3))
    for i in range(n):
        rgb_tuple = rgb_list_of_tuples[i]
        arr[i,0] = rgb_tuple[0]
        arr[i,1] = rgb_tuple[1]
        arr[i,2] = rgb_tuple[2]
    return arr

def matplotlib_linsegcmap_to_rgba(lscmap: matplotlib.colors.LinearSegmentedColormap, nv=256, alpha=False):
    """Convert matplotlib.colors.LinearSegmentedColormap to an rgb(a) array

    :param lscmap: linear segmented colormap
    :type lscmap: matplotlib.colors.LinearSegmentedColormap
    :param nv: number of values in output array. default 256.
    :type nv: int, optional
    :param alpha: whether to also output alpha values. default False.
    :type alpha: bool, optional
    """
    # base = cm.get_cmap(name=nm)
    cs = matplotlib.cm.ScalarMappable(cmap=lscmap)
    c = cs.to_rgba(x=[i for i in range(nv)])
    if not alpha:
        c = c[:,:3]
    return c

def greyscale_RGB(color_rgb):
    """Return greyscale array

    :param color_rgb: iterable of floating point values
    :type color_rgb: tuple
    :return: array of greyscale values.
    :rtype: class `numpy.ndarray`
    """
    greyscale_JCh = cspace_convert(color_rgb, "sRGB1", "JCh")
    greyscale_JCh[...,1] = 0
    tmp_sRGB1 = cspace_convert(greyscale_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp_sRGB1, 0.0, 1.0)

def convertHexIterabletoRGBArray(hex_tuple, alpha=True):
    """Convert an iterable, e.g. list or tuple, of hex strings to an array of rgb(a) values.

    :param hex_tuple: iterable of hex strings
    :type hex_tuple: tuple
    :param alpha: whether to output alpha value. default True
    :type alpha: bool, optional
    :return: array of rgb(a) values
    :rtype: class `numpy.ndarray`
    """
    # convert a list or tuple object into a 2-dimensional array of RGB values
    n = len(hex_tuple)
    if alpha:
        rgb_arr = numpy.zeros(shape=(n,4))
        rgb_arr[:,3] = 1.0
    else:
        rgb_arr = numpy.zeros(shape=(n,3))
    for i in range(n):
        tmp = matplotlib.colors.to_rgb(hex_tuple[i])
        rgb_arr[i, 0] = tmp[0]
        rgb_arr[i, 1] = tmp[1]
        rgb_arr[i, 2] = tmp[2]
    return rgb_arr