"""function to create figures for plotting colormappy arrays
"""
import numpy
from colorspacious import cspace_convert

import matplotlib.cm
import matplotlib.colors
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from colormappy.utils import greyscale_RGB
from colormappy.constants import CIECAM02_J_upper, CIECAM02_J_lower, CIECAM02_C_upper, \
    CIECAM02_C_lower, CIECAM02_h_upper, CIECAM02_h_lower, CIECAM02_Q_upper, CIECAM02_Q_lower, \
    CIECAM02_M_upper, CIECAM02_M_lower, CIECAM02_s_upper, CIECAM02_s_lower, CIECAM02_H_upper, \
    CIECAM02_H_lower, CAM02_UCS_Jp_upper, CAM02_UCS_Jp_lower, CAM02_UCS_ap_upper, \
    CAM02_UCS_ap_lower, CAM02_UCS_bp_upper, CAM02_UCS_bp_lower, CIE1931_XYZ_X_upper, \
    CIE1931_XYZ_X_lower, CIE1931_XYZ_Y_upper, CIE1931_XYZ_Y_lower, CIE1931_XYZ_Z_upper, \
    CIE1931_XYZ_Z_lower, CIE1931_xyY_x_upper, CIE1931_xyY_x_lower, CIE1931_xyY_y_upper, \
    CIE1931_xyY_y_lower, CIE1931_xyY_Y_upper, CIE1931_xyY_Y_lower, CIE1976_Lab_L_upper, \
    CIE1976_Lab_L_lower, CIE1976_Lab_a_upper, CIE1976_Lab_a_lower, CIE1976_Lab_b_upper, \
    CIE1976_Lab_b_lower, CIE1976_LCh_L_upper, CIE1976_LCh_L_lower, CIE1976_LCh_C_upper, \
    CIE1976_LCh_C_lower, CIE1976_LCh_h_upper, CIE1976_LCh_h_lower

def colormappy_figure(color_rgb, color_name='color'):
    fig, ax = plt.subplots(2, sharex=True, figsize=(10, 2))  
    fig.subplots_adjust(bottom=0.5)
    cmap = matplotlib.colors.ListedColormap(color_rgb)
    cb1 = matplotlib.colorbar.ColorbarBase(ax[0], cmap=cmap, orientation='horizontal')
    # cb1.set_label(color_name)

    gry = greyscale_RGB(color_rgb=color_rgb)
    cmap = matplotlib.colors.ListedColormap(gry)
    cb2 = matplotlib.colorbar.ColorbarBase(ax[1], cmap=cmap, orientation='horizontal')
    cb2.set_label(color_name)
    return fig

# use these bounds to set ylim in attributes plot
# plot attributes in other color spaces using matplotlib
def colormappy_attributes(color_rgb, color_name='color'):
    # assert color_rgb is array
    xi = [i for i in range(len(color_rgb))]
    JChQMsH = cspace_convert(color_rgb, "sRGB1", "CIECAM02")
    lightness = JChQMsH.J  # lightness (J)
    chroma = JChQMsH.C  # chroma (C)
    hue_angle = JChQMsH.h  # hue angle (h)
    brightness = JChQMsH.Q  # brightness (Q)
    colorfulness = JChQMsH.M  # colorfulness (M)
    saturation = JChQMsH.s  # saturation (s)
    hue_composition = JChQMsH.H  # hue composition (H)
    
    Jpapbp = cspace_convert(color_rgb, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace

    XYZ1 = cspace_convert(color_rgb, "sRGB1", "XYZ1") # CIE 1931 XYZ color space
    xyY1 = cspace_convert(color_rgb, "sRGB1", "xyY1") # CIE 1931 xyY color space
    Lab = cspace_convert(color_rgb, "sRGB1", "CIELab") # CIE 1976 L*a*b* color space
    LCh = cspace_convert(color_rgb, "sRGB1", "CIELCh") # cylindrical version of CIE 1976 L*a*b* color space; h* is in degrees

    cmap = matplotlib.colors.ListedColormap(color_rgb)
    fig, axs = plt.subplots(7, 3, figsize=(15, 15))
    axs[0,0].scatter(xi,lightness, c=color_rgb)
    axs[0,0].set_ylabel("lightness")
    # set bounds for consistent plotting
    pad = (CIECAM02_J_upper - CIECAM02_J_lower)*0.05
    axs[0,0].set_ylim(CIECAM02_J_lower-pad,CIECAM02_J_upper+pad)

    axs[0,1].scatter(xi,chroma, c=color_rgb)
    axs[0,1].set_ylabel("chroma")
    # set bounds for consistent plotting
    pad = (CIECAM02_C_upper - CIECAM02_C_lower)*0.05
    axs[0,0].set_ylim(CIECAM02_C_lower-pad,CIECAM02_C_upper+pad)

    axs[0,2].scatter(xi,hue_angle, c=color_rgb)
    axs[0,2].set_ylabel("hue angle")
    # set bounds for consistent plotting
    pad = (CIECAM02_h_upper - CIECAM02_h_lower)*0.05
    axs[0,0].set_ylim(CIECAM02_h_lower-pad,CIECAM02_h_upper+pad)

    axs[1,0].scatter(xi,brightness, c=color_rgb)
    axs[1,0].set_ylabel("brightness")
    # set bounds for consistent plotting
    pad = (CIECAM02_Q_upper - CIECAM02_Q_lower)*0.05
    axs[0,0].set_ylim(CIECAM02_Q_lower-pad,CIECAM02_Q_upper+pad)

    axs[1,1].scatter(xi,colorfulness, c=color_rgb)
    axs[1,1].set_ylabel("colorfulness")
    # set bounds for consistent plotting
    pad = (CIECAM02_M_upper - CIECAM02_M_lower)*0.05
    axs[0,0].set_ylim(CIECAM02_M_lower-pad,CIECAM02_M_upper+pad)

    axs[1,2].scatter(xi,saturation, c=color_rgb)
    axs[1,2].set_ylabel("saturation")
    # set bounds for consistent plotting
    pad = (CIECAM02_s_upper - CIECAM02_s_lower)*0.05
    axs[0,0].set_ylim(CIECAM02_s_lower-pad,CIECAM02_s_upper+pad)

    axs[2,0].scatter(xi,Jpapbp[:,0], c=color_rgb)
    axs[2,0].set_ylabel("CAM02-UCS (J')a'b'")
    # set bounds for consistent plotting
    pad = (CAM02_UCS_Jp_upper - CAM02_UCS_Jp_lower)*0.05
    axs[0,0].set_ylim(CAM02_UCS_Jp_lower-pad,CAM02_UCS_Jp_upper+pad)

    axs[2,1].scatter(xi,Jpapbp[:,1], c=color_rgb)
    axs[2,1].set_ylabel("CAM02-UCS J'(a')b'")
    # set bounds for consistent plotting
    pad = (CAM02_UCS_ap_upper - CAM02_UCS_ap_lower)*0.05
    axs[0,0].set_ylim(CAM02_UCS_ap_lower-pad,CAM02_UCS_ap_upper+pad)

    axs[2,2].scatter(xi,Jpapbp[:,2], c=color_rgb)
    axs[2,2].set_ylabel("CAM02-UCS J'a'(b')")
    # set bounds for consistent plotting
    pad = (CAM02_UCS_bp_upper - CAM02_UCS_bp_lower)*0.05
    axs[0,0].set_ylim(CAM02_UCS_bp_lower-pad,CAM02_UCS_bp_upper+pad)

    axs[3,0].scatter(xi,XYZ1[:,0], c=color_rgb)
    axs[3,0].set_ylabel("CIE 1931 (X)YZ")
    # set bounds for consistent plotting
    pad = (CIE1931_XYZ_X_upper - CIE1931_XYZ_X_lower)*0.05
    axs[0,0].set_ylim(CIE1931_XYZ_X_lower-pad,CIE1931_XYZ_X_upper+pad)

    axs[3,1].scatter(xi,XYZ1[:,1], c=color_rgb)
    axs[3,1].set_ylabel("CIE 1931 X(Y)Z")
    # set bounds for consistent plotting
    pad = (CIE1931_XYZ_Y_upper - CIE1931_XYZ_Y_lower)*0.05
    axs[0,0].set_ylim(CIE1931_XYZ_Y_lower-pad,CIE1931_XYZ_Y_upper+pad)

    axs[3,2].scatter(xi,XYZ1[:,2], c=color_rgb)
    axs[3,2].set_ylabel("CIE 1931 XY(Z)")
    # set bounds for consistent plotting
    pad = (CIE1931_XYZ_Z_upper - CIE1931_XYZ_Z_lower)*0.05
    axs[0,0].set_ylim(CIE1931_XYZ_Z_lower-pad,CIE1931_XYZ_Z_upper+pad)

    axs[4,0].scatter(xi,xyY1[:,0], c=color_rgb)
    axs[4,0].set_ylabel("CIE 1931 (x)yY")
    # set bounds for consistent plotting
    pad = (CIE1931_xyY_x_upper - CIE1931_xyY_x_lower)*0.05
    axs[0,0].set_ylim(CIE1931_xyY_x_lower-pad,CIE1931_xyY_x_upper+pad)

    axs[4,1].scatter(xi,xyY1[:,1], c=color_rgb)
    axs[4,1].set_ylabel("CIE 1931 x(y)Y")
    # set bounds for consistent plotting
    pad = (CIE1931_xyY_y_upper - CIE1931_xyY_y_lower)*0.05
    axs[0,0].set_ylim(CIE1931_xyY_y_lower-pad,CIE1931_xyY_y_upper+pad)

    axs[4,2].scatter(xi,xyY1[:,2], c=color_rgb)
    axs[4,2].set_ylabel("CIE 1931 xy(Y)")
    # set bounds for consistent plotting
    pad = (CIE1931_xyY_Y_upper - CIE1931_xyY_Y_lower)*0.05
    axs[0,0].set_ylim(CIE1931_xyY_Y_lower-pad,CIE1931_xyY_Y_upper+pad)

    axs[5,0].scatter(xi,Lab[:,0], c=color_rgb)
    axs[5,0].set_ylabel("CIE 1976 (L*)a*b*")
    # set bounds for consistent plotting
    pad = (CIE1976_Lab_L_upper - CIE1976_Lab_L_lower)*0.05
    axs[0,0].set_ylim(CIE1976_Lab_L_lower-pad,CIE1976_Lab_L_upper+pad)

    axs[5,1].scatter(xi,Lab[:,1], c=color_rgb)
    axs[5,1].set_ylabel("CIE 1976 L*(a*)b*")
    # set bounds for consistent plotting
    pad = (CIE1976_Lab_a_upper - CIE1976_Lab_a_lower)*0.05
    axs[0,0].set_ylim(CIE1976_Lab_a_lower-pad,CIE1976_Lab_a_upper+pad)

    axs[5,2].scatter(xi,Lab[:,2], c=color_rgb)
    axs[5,2].set_ylabel("CIE 1976 L*a*(b*)")
    # set bounds for consistent plotting
    pad = (CIE1976_Lab_b_upper - CIE1976_Lab_b_lower)*0.05
    axs[0,0].set_ylim(CIE1976_Lab_b_lower-pad,CIE1976_Lab_b_upper+pad)

    axs[6,0].scatter(xi,LCh[:,0], c=color_rgb)
    axs[6,0].set_ylabel("CIE 1976 (L)Ch")
    # set bounds for consistent plotting
    pad = (CIE1976_LCh_L_upper - CIE1976_LCh_L_lower)*0.05
    axs[0,0].set_ylim(CIE1976_LCh_L_lower-pad,CIE1976_LCh_L_upper+pad)

    axs[6,1].scatter(xi,LCh[:,1], c=color_rgb)
    axs[6,1].set_ylabel("CIE 1976 L(C)h")
    # set bounds for consistent plotting
    pad = (CIE1976_LCh_C_upper - CIE1976_LCh_C_lower)*0.05
    axs[0,0].set_ylim(CIE1976_LCh_C_lower-pad,CIE1976_LCh_C_upper+pad)

    axs[6,2].scatter(xi,LCh[:,2], c=color_rgb)
    axs[6,2].set_ylabel("CIE 1976 LC(h)")
    # set bounds for consistent plotting
    pad = (CIE1976_LCh_h_upper - CIE1976_LCh_h_lower)*0.05
    axs[0,0].set_ylim(CIE1976_LCh_h_lower-pad,CIE1976_LCh_h_upper+pad)

    fig.subplots_adjust(hspace=0.6, wspace=0.2)
    fig.suptitle("colormap attributes - " + color_name)
    return fig

def scatter3D_Jpapbp(color_rgb, color_name='color'):
    fig = plt.figure(figsize = (12, 8))
    ax = plt.axes(projection ="3d")
 
    Jpapbp = cspace_convert(color_rgb, "sRGB1", "CAM02-UCS")  # J'a'b' LuoEtAl2006UniformSpace
    x = Jpapbp[:,0]  # J'
    y = Jpapbp[:,1]  # a'
    z = Jpapbp[:,2]  # b'
    
    # Creating plot
    sctt = ax.scatter3D(x, y, z, 
        #alpha = 0.8,
        c = [i for i in range(Jpapbp.shape[0])],
        cmap = matplotlib.colors.ListedColormap(color_rgb),
        #marker ='^'
    )
 
    plt.title("CAM02-UCS color space - " + color_name)
    ax.set_xlabel("J'", fontweight ='bold')
    ax.set_ylabel("a'", fontweight ='bold')
    ax.set_zlabel("b'", fontweight ='bold')
    fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 10)

    return fig

def surface_sombrero(color_rgb, color_name='color'):
    
    x = numpy.arange(-10,10,0.01)
    y = numpy.arange(-10,10,0.01)
    x,y = numpy.meshgrid(x,y)
    a = numpy.sqrt(numpy.square(x) + numpy.square(y))
    z = numpy.sin(a) / a

    fig = plt.figure(figsize = (12, 8))
    ax = plt.axes(projection ="3d")
    surf = ax.plot_surface(x, y, z, cmap=matplotlib.colors.ListedColormap(color_rgb),
        linewidth=0, antialiased=False)

    plt.title("sombrero 2d kernel - " + color_name)
    fig.colorbar(surf, ax = ax, shrink = 0.5, aspect = 10)
    
    return fig