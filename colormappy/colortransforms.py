"""Color transforms
"""

import colorsys
import numpy

from colorspacious import cspace_convert

def hls_full_saturation(color_rgb):
    # color_rgb is a list or tuple of length 3
    # create natural color, i.e full saturation and neither tinted nor shaded
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    # set the lightnessto 0.5, i.e. 50% and the saturation to 1.0, i.e. 100%
    saturated_hls = (color_hls[0], 0.5, 1.0)
    # return (r,g,b)
    return colorsys.hls_to_rgb(h=saturated_hls[0], l=saturated_hls[1], s=saturated_hls[2])

def hls_saturate(color_rgb, quantile=0.5):
    # increase saturation
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    sat = (1.0 - color_hls[2]) * quantile
    saturated_hls = (color_hls[0], color_hls[1], color_hls[2]+sat)
    return colorsys.hls_to_rgb(h=saturated_hls[0], l=saturated_hls[1], s=saturated_hls[2])

def hls_desaturate(color_rgb, quantile=0.5):
    # decrease saturation, i.e. move towards grey
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    sat = color_hls[2] * quantile
    saturated_hls = (color_hls[0], color_hls[1], color_hls[2]-sat)
    return colorsys.hls_to_rgb(h=saturated_hls[0], l=saturated_hls[1], s=saturated_hls[2])

def hls_complementary_color(color_rgb):
    # return the complementary color
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    h = color_hls[0]
    if h <= 0.5:
        h = h + 0.5
    else:
        h = h - 0.5
    complementary_hls = (h, color_hls[1], color_hls[2])
    return colorsys.hls_to_rgb(h=complementary_hls[0], l=complementary_hls[1], s=complementary_hls[2])

def hls_mix_colors(color1_rgb, color2_rgb, quantile=0.5):
    color1_hls = colorsys.rgb_to_hls(r=color1_rgb[0], g=color1_rgb[1], b=color1_rgb[2])
    color2_hls = colorsys.rgb_to_hls(r=color2_rgb[0], g=color2_rgb[1], b=color2_rgb[2])
    h = ((1.0 - quantile) * color1_hls[0]) + (quantile * color2_hls[0])
    l = ((1.0 - quantile) * color1_hls[0]) + (quantile * color2_hls[0])
    s = ((1.0 - quantile) * color1_hls[0]) + (quantile * color2_hls[0])
    return colorsys.hls_to_rgb(h=h, l=l, s=s)

def hls_lighten(color_rgb, quantile=0.5):
    # tint - mix white
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    white_hls = (0.0, 1.0, 0.0)
    # h = ((1.0 - quantile) * color_hls[0]) + (quantile * white_hls[0])
    l = ((1.0 - quantile) * color_hls[1]) + (quantile * white_hls[1])
    # s = ((1.0 - quantile) * color_hls[2]) + (quantile * white_hls[2])
    return colorsys.hls_to_rgb(h=color_hls[0], l=l, s=color_hls[2])

def hls_darken(color_rgb, quantile=0.5):
    # shade - mix black
    color_hls = colorsys.rgb_to_hls(r=color_rgb[0], g=color_rgb[1], b=color_rgb[2])
    black_hls = (0.0, 0.0, 0.0)
    # h = ((1.0 - quantile) * color_hls[0]) + (quantile * white_hls[0])
    l = ((1.0 - quantile) * color_hls[1]) + (quantile * black_hls[1])
    # s = ((1.0 - quantile) * color_hls[2]) + (quantile * white_hls[2])
    return colorsys.hls_to_rgb(h=color_hls[0], l=l, s=color_hls[2])

# shading, tinting, and toning via interpolation with black, white, or grey in uniform color space
def Jpapbp_darken(base_rgb, quantile=0.5):
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
    base_LCh = cspace_convert(base_rgb, "sRGB1", "CIELCh")
    comp_LCh = numpy.copy(base_LCh)
    comp_LCh[2] = base_LCh[2] + 180
    if comp_LCh[2] > 360:
        comp_LCh[2] -= 360
    comp_sRGB1 = cspace_convert(comp_LCh, "CIELCh", "sRGB1")
    comp_sRGB1 = numpy.clip(comp_sRGB1, 0.0, 1.0)
    return (comp_sRGB1[0], comp_sRGB1[1], comp_sRGB1[2])

def CIELCh_darken(base_rgb, quantile=0.5):
    # shade - mix black
    base_LCh = cspace_convert(base_rgb, "sRGB1", "CIELCh")
    # black_LCh = cspace_convert((0.0,0.0,0.0), "sRGB1", "CIELCh")
    # print(black_LCh) [0. 0. 0.]
    color_LCh = numpy.copy(base_LCh)
    color_LCh[0] = base_LCh[0] - (quantile * base_LCh[0])
    
    color_sRGB1 = cspace_convert(color_LCh, "CIELCh", "sRGB1")
    color_sRGB1 = numpy.clip(color_sRGB1, 0.0, 1.0)
    return (color_sRGB1[0], color_sRGB1[1], color_sRGB1[2])

def CIELCh_lighten(base_rgb, quantile=0.5):
    # shade - mix black
    base_LCh = cspace_convert(base_rgb, "sRGB1", "CIELCh")
    white_LCh = cspace_convert((1.0,1.0,1.0), "sRGB1", "CIELCh")
    # print(white_LCh) #[ 99.99833859   0.0140741  301.97810937]
    color_LCh = numpy.copy(base_LCh)
    color_LCh[0] = base_LCh[0] + (quantile * (white_LCh[0] - base_LCh[0]))
    
    color_sRGB1 = cspace_convert(color_LCh, "CIELCh", "sRGB1")
    color_sRGB1 = numpy.clip(color_sRGB1, 0.0, 1.0)
    return (color_sRGB1[0], color_sRGB1[1], color_sRGB1[2])

def Jpapbp_neutral(base_rgb, quantile=0.5):
    # mix the base rgb with its complementary color
    # TODO: assert quantile between 0 and 1
    comp_rgb = CIELCh_complementary(base_rgb=base_rgb)
    # 1/2 is a maxium where base and comp are mixed equally yileding a grey
    return Jpapbp_mix_colors(color1_rgb=base_rgb, color2_rgb=comp_rgb, quantile=0.5 * quantile)

# https://colorspacious.readthedocs.io/en/latest/tutorial.html
def JCh_desaturate(base_rgb, quantile=0.5):
    # reduce the "C" value (Chroma)
    base_JCh = cspace_convert(base_rgb, "sRGB1", "JCh")
    base_JCh[..., 1] *= quantile
    tmp = cspace_convert(base_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)

def JCh_saturate(base_rgb, quantile=0.5):
    # reduce the "C" value (chroma)
    base_JCh = cspace_convert(base_rgb, "sRGB1", "JCh")
    base_JCh[..., 1] *= (1 + quantile)
    tmp = cspace_convert(base_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)

def JCh_darken(base_rgb, quantile=0.5):
    # reduce the "J" value (lightness)
    base_JCh = cspace_convert(base_rgb, "sRGB1", "JCh")
    base_JCh[..., 0] *= quantile
    tmp = cspace_convert(base_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)

def JCh_lighten(base_rgb, quantile=0.5):
    # reduce the "J" value (lightness)
    base_JCh = cspace_convert(base_rgb, "sRGB1", "JCh")
    base_JCh[..., 0] *= (1 + quantile)
    tmp = cspace_convert(base_JCh, "JCh", "sRGB1")
    return numpy.clip(tmp, 0.0, 1.0)