from mpl_context import colormappy

import matplotlib.pyplot as plt
import matplotlib.cm as cm

from colormappy.utils import matplotlib_linsegcmap_to_rgba
from colormappy_plotting import colormappy_figure, colormappy_attributes, scatter3D_Jpapbp, surface_sombrero

mappy_cmap = cm.get_cmap(name='Dark2')
mappy_rgb = matplotlib_linsegcmap_to_rgba(mappy_cmap, 256, False)

mappy_name = 'matplotlib Dark2'
fig = colormappy_figure(mappy_rgb, color_name=mappy_name)
fig = colormappy_attributes(mappy_rgb, color_name=mappy_name)
fig = scatter3D_Jpapbp(mappy_rgb, color_name=mappy_name)
fig = surface_sombrero(mappy_rgb, color_name=mappy_name)

plt.show()