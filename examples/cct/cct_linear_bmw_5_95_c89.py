from cct_context import colormappy

import matplotlib.pyplot as plt
import colorcet

from colormappy.utils import matplotlib_linsegcmap_to_rgba
from colormappy_plotting import colormappy_figure, colormappy_attributes, scatter3D_Jpapbp, surface_sombrero

cct_id = 'linear_bmw_5_95_c89'
mappy_rgb = matplotlib_linsegcmap_to_rgba(colorcet.cm[cct_id], 256, False)
mappy_name = f'colorcet - {cct_id}_rgb'
fig = colormappy_figure(mappy_rgb, color_name=mappy_name)
fig = colormappy_attributes(mappy_rgb, color_name=mappy_name)
fig = scatter3D_Jpapbp(mappy_rgb, color_name=mappy_name)
fig = surface_sombrero(mappy_rgb, color_name=mappy_name)

plt.show()