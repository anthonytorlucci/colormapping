'''color interpolation

create a colormap between the colors cyan and magenta in various colorspaces
'''

import matplotlib.pyplot as plt
import matplotlib.colors

import colormappy.colors as clrs
import colormappy

cyan = clrs.rgb1_Cyan
magenta = clrs.rgb1_Magenta

p0 = colormappy.ColorPointIndex(idx=0, c0=cyan[0], c1=cyan[1], c2=cyan[2], cspace="sRGB1")
p255 = colormappy.ColorPointIndex(idx=255, c0=magenta[0], c1=magenta[1], c2=magenta[2], cspace="sRGB1")

spaces = ["XYZ1", "xyY1", "CAM02-UCS", "CIELab", "CIELCh", 
    "JCh", "JMh", "Jsh", "JCH", "JMH", "JsH", "QCh", "QMh", 
    "Qsh", "QCH", "QMH", "QsH"]

nspaces = len(spaces)

fig, ax = plt.subplots(nspaces, sharex=True, figsize=(10,17))

for n in range(nspaces):
    space = spaces[n]
    mappy = colormappy.create_colormap(points=[p0, p255], interp_cspace=space)
    cmap = matplotlib.colors.ListedColormap(mappy)
    cb1 = matplotlib.colorbar.ColorbarBase(ax[n], cmap=cmap, orientation='horizontal')
    cb1.set_label(space)

fig.tight_layout()
# fig.show()
plt.show()