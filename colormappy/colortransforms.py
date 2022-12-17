"""Color transforms
"""

# standard
import colorsys

# third party
import numpy
from colorspacious import cspace_convert

def hls_full_saturation(color_rgb):
    """
    Create natural color, i.e. full saturation and neither tinted nor shaded from the given rgb values, in the hls color space.

    Parameters:
    -----------
    color_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1). 
    """
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    # set the lightnessto 0.5, i.e. 50% and the saturation to 1.0, i.e. 100%
    saturated_hls = (color_hls[0], 0.5, 1.0)
    return colorsys.hls_to_rgb(h=saturated_hls[0], l=saturated_hls[1], s=saturated_hls[2])

def hls_saturate(color_rgb, quantile=0.5):
    """
    Increase the saturation from the given rgb values in the hls color space.

    Parameters:
    -----------
    color_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1). 
    quantile : float, default=0.5
        Quantile value to increase the saturation.
    """
    # increase saturation
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    sat = (1.0 - color_hls[2]) * quantile
    saturated_hls = (color_hls[0], color_hls[1], color_hls[2]+sat)
    return colorsys.hls_to_rgb(h=saturated_hls[0], l=saturated_hls[1], s=saturated_hls[2])

def hls_desaturate(color_rgb, quantile=0.5):
    """
    Decrease saturation, i.e. move towards gray, in the hls color space.

    Parameters
    ----------
    color_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1). 
    quantile : float, default=0.5
        Quantile value to decrease the saturation.
    """
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    sat = color_hls[2] * quantile
    saturated_hls = (color_hls[0], color_hls[1], color_hls[2]-sat)
    return colorsys.hls_to_rgb(h=saturated_hls[0], l=saturated_hls[1], s=saturated_hls[2])

def hls_complementary_color(color_rgb):
    """
    Get the complementary color in the hls color space.

    Parameters
    ----------
    color_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    """
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    h = color_hls[0]
    if h <= 0.5:
        h = h + 0.5
    else:
        h = h - 0.5
    complementary_hls = (h, color_hls[1], color_hls[2])
    return colorsys.hls_to_rgb(h=complementary_hls[0], l=complementary_hls[1], s=complementary_hls[2])

def hls_mix_colors(color1_rgb, color2_rgb, quantile=0.5):
    """
    Mix two colors in the hls color space.

    Parameters
    ----------
    color1_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    color2_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile of the second color, color2_rgb, when combined. 0.5 will mix each color equally.
    """
    color1_hls = colorsys.rgb_to_hls(r=color1_rgb[0], g=color1_rgb[1], b=color1_rgb[2])
    color2_hls = colorsys.rgb_to_hls(r=color2_rgb[0], g=color2_rgb[1], b=color2_rgb[2])
    h = ((1.0 - quantile) * color1_hls[0]) + (quantile * color2_hls[0])
    l = ((1.0 - quantile) * color1_hls[0]) + (quantile * color2_hls[0])
    s = ((1.0 - quantile) * color1_hls[0]) + (quantile * color2_hls[0])
    return colorsys.hls_to_rgb(h=h, l=l, s=s)

def hls_lighten(color_rgb, quantile=0.5):
    """
    Tint or mix with white in the hls color space.

    Parameters
    ----------
    color_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount of white to be mixed or combined.
    """
    # tint - mix white
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    white_hls = (0.0, 1.0, 0.0)
    # h = ((1.0 - quantile) * color_hls[0]) + (quantile * white_hls[0])
    l = ((1.0 - quantile) * color_hls[1]) + (quantile * white_hls[1])
    # s = ((1.0 - quantile) * color_hls[2]) + (quantile * white_hls[2])
    return colorsys.hls_to_rgb(h=color_hls[0], l=l, s=color_hls[2])

def hls_darken(color_rgb, quantile=0.5):
    """
    Shade or mix with black in the hls color space.

    Parameters
    ----------
    color_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount of blak to be mixed or combined.
    """
    # shade - mix black
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    black_hls = (0.0, 0.0, 0.0)
    # h = ((1.0 - quantile) * color_hls[0]) + (quantile * white_hls[0])
    l = ((1.0 - quantile) * color_hls[1]) + (quantile * black_hls[1])
    # s = ((1.0 - quantile) * color_hls[2]) + (quantile * white_hls[2])
    return colorsys.hls_to_rgb(h=color_hls[0], l=l, s=color_hls[2])

# shading, tinting, and toning via interpolation with black, white, or grey in uniform color space
def Jpapbp_darken(base_rgb, quantile=0.5):
    """
    Darken via interpolation between given color and black in the J'a'b' Luo et al. 2006 Uniform color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount, or distance from black in J'a'b', to given color base in J'a'b'.
    """
    # TODO: assert quantile between 0 and 1
    base_Jpapbp = cspace_convert(base_rgb, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace
    black_Jpapbp = cspace_convert([0.0,0.0,0.0], "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace

    xp = [0.0, 1.0]
    yp0 = [base_Jpapbp[0], black_Jpapbp[0]]
    yp1 = [base_Jpapbp[1], black_Jpapbp[1]]
    yp2 = [base_Jpapbp[2], black_Jpapbp[2]]

    interpolated_color_index0 = numpy.interp(quantile, xp, yp0)
    interpolated_color_index1 = numpy.interp(quantile, xp, yp1)
    interpolated_color_index2 = numpy.interp(quantile, xp, yp2)
    interpolated_color = [interpolated_color_index0, interpolated_color_index1, interpolated_color_index2]
    interpolated_color = cspace_convert(interpolated_color, "CAM02-UCS", "sRGB1")
    
    interpolated_color = numpy.clip(interpolated_color, 0.0, 1.0)
    return (interpolated_color[0], interpolated_color[1], interpolated_color[2])

def Jpapbp_lighten(base_rgb, quantile=0.5):
    """
    Lighten via interpolation between given color and white in the J'a'b' Luo et al. 2006 Uniform color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount, or distance from white in J'a'b', to given color base in J'a'b'.
    """
    # TODO: assert quantile between 0 and 1
    base_Jpapbp = cspace_convert(base_rgb, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace
    white_Jpapbp = cspace_convert([1.0,1.0,1.0], "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace

    xp = [0.0, 1.0]
    yp0 = [base_Jpapbp[0], white_Jpapbp[0]]
    yp1 = [base_Jpapbp[1], white_Jpapbp[1]]
    yp2 = [base_Jpapbp[2], white_Jpapbp[2]]

    interpolated_color_index0 = numpy.interp(quantile, xp, yp0)
    interpolated_color_index1 = numpy.interp(quantile, xp, yp1)
    interpolated_color_index2 = numpy.interp(quantile, xp, yp2)
    interpolated_color = [interpolated_color_index0, interpolated_color_index1, interpolated_color_index2]
    interpolated_color = cspace_convert(interpolated_color, "CAM02-UCS", "sRGB1")
    
    interpolated_color = numpy.clip(interpolated_color, 0.0, 1.0)
    return (interpolated_color[0], interpolated_color[1], interpolated_color[2])

def Jpapbp_tone(base_rgb, quantile=0.5):
    """
    Tone via interpolation between given color and gray in the J'a'b' Luo et al. 2006 Uniform color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount, or distance from gray in J'a'b', to given color base in J'a'b'.
    """
    # TODO: assert quantile between 0 and 1
    base_Jpapbp = cspace_convert(base_rgb, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace
    grey_Jpapbp = cspace_convert([0.5,0.5,0.5], "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace

    xp = [0.0, 1.0]
    yp0 = [base_Jpapbp[0], grey_Jpapbp[0]]
    yp1 = [base_Jpapbp[1], grey_Jpapbp[1]]
    yp2 = [base_Jpapbp[2], grey_Jpapbp[2]]

    interpolated_color_index0 = numpy.interp(quantile, xp, yp0)
    interpolated_color_index1 = numpy.interp(quantile, xp, yp1)
    interpolated_color_index2 = numpy.interp(quantile, xp, yp2)
    interpolated_color = [interpolated_color_index0, interpolated_color_index1, interpolated_color_index2]
    interpolated_color = cspace_convert(interpolated_color, "CAM02-UCS", "sRGB1")
    
    interpolated_color = numpy.clip(interpolated_color, 0.0, 1.0)
    return (interpolated_color[0], interpolated_color[1], interpolated_color[2])

def Jpapbp_mix_colors(color1_rgb, color2_rgb, quantile=0.5):
    """
    Mix two colors in the J'a'b' color space. See colorspacious python package for more information.

    Parameters
    ----------
    color1_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    color2_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile of the second color, color2_rgb, when combined. 0.5 will mix each color equally.
    """
    # TODO: assert quantile between 0 and 1
    color1_Jpapbp = cspace_convert(color1_rgb, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace
    color2_Jpapbp = cspace_convert(color2_rgb, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace

    xp = [0.0, 1.0]
    yp0 = [color1_Jpapbp[0], color2_Jpapbp[0]]
    yp1 = [color1_Jpapbp[1], color2_Jpapbp[1]]
    yp2 = [color1_Jpapbp[2], color2_Jpapbp[2]]

    interpolated_color_index0 = numpy.interp(quantile, xp, yp0)
    interpolated_color_index1 = numpy.interp(quantile, xp, yp1)
    interpolated_color_index2 = numpy.interp(quantile, xp, yp2)
    interpolated_color = [interpolated_color_index0, interpolated_color_index1, interpolated_color_index2]
    interpolated_color = cspace_convert(interpolated_color, "CAM02-UCS", "sRGB1")
    
    interpolated_color = numpy.clip(interpolated_color, 0.0, 1.0)
    return (interpolated_color[0], interpolated_color[1], interpolated_color[2])

def CIELCh_complementary(base_rgb):
    """
    Complementary color in the CIELCh color space. See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    """
    base_LCh = cspace_convert(base_rgb, "sRGB1", "CIELCh")
    comp_LCh = numpy.copy(base_LCh)
    comp_LCh[2] = base_LCh[2] + 180
    if comp_LCh[2] > 360:
        comp_LCh[2] -= 360
    comp_sRGB1 = cspace_convert(comp_LCh, "CIELCh", "sRGB1")
    comp_sRGB1 = numpy.clip(comp_sRGB1, 0.0, 1.0)
    return (comp_sRGB1[0], comp_sRGB1[1], comp_sRGB1[2])

def CIELCh_darken(base_rgb, quantile=0.5):
    """
    Darken, i.e. shade, in the CIELCh color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount of black combined with given color in CIELCh color space.
    """
    base_LCh = cspace_convert(base_rgb, "sRGB1", "CIELCh")
    # black_LCh = cspace_convert((0.0,0.0,0.0), "sRGB1", "CIELCh")
    # print(black_LCh) [0. 0. 0.]
    color_LCh = numpy.copy(base_LCh)
    color_LCh[0] = base_LCh[0] - (quantile * base_LCh[0])
    
    color_sRGB1 = cspace_convert(color_LCh, "CIELCh", "sRGB1")
    color_sRGB1 = numpy.clip(color_sRGB1, 0.0, 1.0)
    return (color_sRGB1[0], color_sRGB1[1], color_sRGB1[2])

def CIELCh_lighten(base_rgb, quantile=0.5):
    """
    Lighten in the CIELCh color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount of white combined with given color in CIELCh color space.
    """
    base_LCh = cspace_convert(base_rgb, "sRGB1", "CIELCh")
    white_LCh = cspace_convert((1.0,1.0,1.0), "sRGB1", "CIELCh")
    # print(white_LCh) #[ 99.99833859   0.0140741  301.97810937]
    color_LCh = numpy.copy(base_LCh)
    color_LCh[0] = base_LCh[0] + (quantile * (white_LCh[0] - base_LCh[0]))
    
    color_sRGB1 = cspace_convert(color_LCh, "CIELCh", "sRGB1")
    color_sRGB1 = numpy.clip(color_sRGB1, 0.0, 1.0)
    return (color_sRGB1[0], color_sRGB1[1], color_sRGB1[2])

def Jpapbp_neutral(base_rgb, quantile=0.5):
    """
    Mix or combine the base_rgb with its complimentary color in the J'a'b' color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount.
    """
    # mix the base rgb with its complementary color
    # TODO: assert quantile between 0 and 1
    comp_rgb = CIELCh_complementary(base_rgb=base_rgb)
    # 1/2 is a maxium where base and comp are mixed equally yileding a grey
    return Jpapbp_mix_colors(color1_rgb=base_rgb, color2_rgb=comp_rgb, quantile=0.5 * quantile)

# https://colorspacious.readthedocs.io/en/latest/tutorial.html
def JCh_desaturate(base_rgb, quantile=0.5):
    """
    Desaturate in JCh color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount.
    """
    # reduce the "C" value (Chroma)
    base_JCh = cspace_convert(base_rgb, "sRGB1", "JCh")
    base_JCh[..., 1] *= quantile
    tmp = cspace_convert(base_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)

def JCh_saturate(base_rgb, quantile=0.5):
    """
    Saturate in JCh color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount.
    """
    # reduce the "C" value (chroma)
    base_JCh = cspace_convert(base_rgb, "sRGB1", "JCh")
    base_JCh[..., 1] *= (1 + quantile)
    tmp = cspace_convert(base_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)

def JCh_darken(base_rgb, quantile=0.5):
    """
    Darken in JCh color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount.
    """
    # reduce the "J" value (lightness)
    base_JCh = cspace_convert(base_rgb, "sRGB1", "JCh")
    base_JCh[..., 0] *= quantile
    tmp = cspace_convert(base_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)

def JCh_lighten(base_rgb, quantile=0.5):
    """
    Lighten in JCh color space.
    See colorspacious python package for more information.

    Parameters
    ----------
    base_rgb : tuple, list
        Tuple or list of length 3 in which index 0 corresponds to red, index 1 corresponds to green, and index 2 corresponds to blue. The values should be in the range (0,1).
    quantile : float, default=0.5
        Quantile amount.
    """
    # reduce the "J" value (lightness)
    base_JCh = cspace_convert(base_rgb, "sRGB1", "JCh")
    base_JCh[..., 0] *= (1 + quantile)
    tmp = cspace_convert(base_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)