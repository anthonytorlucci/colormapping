from sc7_context import colormappy

import matplotlib.pyplot as plt
import numpy

from colormappy_plotting import colormappy_figure, colormappy_attributes, scatter3D_Jpapbp, surface_sombrero

batlowK_cmdata = [
    [0.010753, 0.014697, 0.019692],      
    [0.014705, 0.022477, 0.03011],      
    [0.018513, 0.030323, 0.04078],      
    [0.022378, 0.038435, 0.050426],      
    [0.026306, 0.046036, 0.059125],      
    [0.030304, 0.053084, 0.06696],      
    [0.034413, 0.059722, 0.074236],      
    [0.038727, 0.065759, 0.081005],      
    [0.042807, 0.071572, 0.087422],      
    [0.046912, 0.076977, 0.093391],      
    [0.050665, 0.082318, 0.099291],      
    [0.054034, 0.087386, 0.10526],      
    [0.057094, 0.092252, 0.11141],      
    [0.05984, 0.096955, 0.11757],      
    [0.061906, 0.10176, 0.12384],      
    [0.063619, 0.10678, 0.13024],      
    [0.065295, 0.11181, 0.13657],      
    [0.06704, 0.11691, 0.14304],      
    [0.068875, 0.12209, 0.14953],      
    [0.070634, 0.1274, 0.15603],      
    [0.072509, 0.13277, 0.16255],      
    [0.074477, 0.1382, 0.1691],      
    [0.076456, 0.14367, 0.17559],      
    [0.078557, 0.1492, 0.18211],      
    [0.08079, 0.15478, 0.18864],      
    [0.08306, 0.16039, 0.19509],      
    [0.085423, 0.16608, 0.20148],      
    [0.087972, 0.17179, 0.20785],      
    [0.090567, 0.17755, 0.21413],      
    [0.093232, 0.18326, 0.22033],      
    [0.096073, 0.18904, 0.22641],      
    [0.099048, 0.19481, 0.23238],      
    [0.10212, 0.20053, 0.23822],      
    [0.1053, 0.20632, 0.24391],      
    [0.10861, 0.21204, 0.24948],      
    [0.11209, 0.21772, 0.2549],      
    [0.11562, 0.22338, 0.26011],      
    [0.11926, 0.22899, 0.26513],      
    [0.12299, 0.23455, 0.27],      
    [0.12686, 0.24002, 0.27462],      
    [0.13085, 0.24544, 0.27907],      
    [0.13488, 0.2508, 0.28328],      
    [0.13895, 0.25605, 0.28725],      
    [0.14314, 0.26123, 0.29103],      
    [0.14738, 0.26631, 0.29454],      
    [0.15164, 0.27127, 0.29784],      
    [0.156, 0.27615, 0.30089],      
    [0.16032, 0.28087, 0.30371],      
    [0.16473, 0.28551, 0.30632],      
    [0.16917, 0.29003, 0.30866],      
    [0.17356, 0.29443, 0.31077],      
    [0.17802, 0.29872, 0.31264],      
    [0.1824, 0.30286, 0.3143],      
    [0.18684, 0.30692, 0.31575],      
    [0.19125, 0.31085, 0.31696],      
    [0.19566, 0.31463, 0.31798],      
    [0.20004, 0.31833, 0.31879],      
    [0.20446, 0.3219, 0.31941],      
    [0.2088, 0.32536, 0.31985],      
    [0.21314, 0.32875, 0.3201],      
    [0.21749, 0.33201, 0.32019],      
    [0.22179, 0.33519, 0.3201],      
    [0.22611, 0.33826, 0.31986],      
    [0.23037, 0.34126, 0.31947],      
    [0.23468, 0.34417, 0.31894],      
    [0.23892, 0.34704, 0.31828],      
    [0.24318, 0.34981, 0.31749],      
    [0.24745, 0.35253, 0.31659],      
    [0.25171, 0.3552, 0.31557],      
    [0.25594, 0.3578, 0.31443],      
    [0.26021, 0.36034, 0.31322],      
    [0.26447, 0.36286, 0.31188],      
    [0.26875, 0.36534, 0.3105],      
    [0.27302, 0.36778, 0.30901],      
    [0.27732, 0.37019, 0.30742],      
    [0.28162, 0.37258, 0.30579],      
    [0.28592, 0.37495, 0.30406],      
    [0.29027, 0.37729, 0.30228],      
    [0.29463, 0.37962, 0.30045],      
    [0.29902, 0.38193, 0.29856],      
    [0.30341, 0.38423, 0.29663],      
    [0.30783, 0.38652, 0.29463],      
    [0.31228, 0.38881, 0.2926],      
    [0.31677, 0.3911, 0.29052],      
    [0.32127, 0.39336, 0.28841],      
    [0.32579, 0.39565, 0.28626],      
    [0.33036, 0.39792, 0.28409],      
    [0.33497, 0.4002, 0.28189],      
    [0.33958, 0.40247, 0.27966],      
    [0.34422, 0.40476, 0.2774],      
    [0.34892, 0.40706, 0.27512],      
    [0.35364, 0.40936, 0.27281],      
    [0.35841, 0.41166, 0.27051],      
    [0.36322, 0.41398, 0.26816],      
    [0.36806, 0.41631, 0.26583],      
    [0.37295, 0.41864, 0.26348],      
    [0.37788, 0.42099, 0.2611],      
    [0.38286, 0.42335, 0.25874],      
    [0.38788, 0.42573, 0.25635],      
    [0.39296, 0.42813, 0.25398],      
    [0.39809, 0.43053, 0.2516],      
    [0.40326, 0.43294, 0.24921],      
    [0.40848, 0.43538, 0.24683],      
    [0.41376, 0.43782, 0.24444],      
    [0.4191, 0.44027, 0.24209],      
    [0.42449, 0.44275, 0.23974],      
    [0.42993, 0.44523, 0.23742],      
    [0.43545, 0.44772, 0.23509],      
    [0.441, 0.45024, 0.23276],      
    [0.44663, 0.45277, 0.23048],      
    [0.45232, 0.4553, 0.22825],      
    [0.45805, 0.45784, 0.22603],      
    [0.46386, 0.46039, 0.22382],      
    [0.46974, 0.46296, 0.22167],      
    [0.47567, 0.46554, 0.21957],      
    [0.48166, 0.46812, 0.21752],      
    [0.48772, 0.47072, 0.21551],      
    [0.49384, 0.47331, 0.21356],      
    [0.50003, 0.47592, 0.2117],      
    [0.50628, 0.47852, 0.20987],      
    [0.51261, 0.48112, 0.20814],      
    [0.51901, 0.48373, 0.20651],      
    [0.52546, 0.48634, 0.20493],      
    [0.53198, 0.48895, 0.20346],      
    [0.53857, 0.49157, 0.20208],      
    [0.54522, 0.49416, 0.20082],      
    [0.55193, 0.49675, 0.19968],      
    [0.5587, 0.49934, 0.19867],      
    [0.56554, 0.50192, 0.19779],      
    [0.57244, 0.5045, 0.19706],      
    [0.5794, 0.50704, 0.19647],      
    [0.5864, 0.50958, 0.196],      
    [0.59346, 0.51211, 0.1957],      
    [0.60057, 0.51462, 0.19558],      
    [0.60772, 0.51711, 0.19563],      
    [0.61491, 0.51957, 0.19586],      
    [0.62214, 0.52201, 0.19629],      
    [0.62941, 0.52443, 0.19689],      
    [0.63671, 0.52684, 0.19766],      
    [0.64402, 0.5292, 0.19865],      
    [0.65136, 0.53153, 0.19983],      
    [0.65871, 0.53383, 0.20123],      
    [0.66607, 0.53612, 0.20284],      
    [0.67344, 0.53837, 0.20467],      
    [0.68081, 0.54058, 0.20669],      
    [0.68818, 0.54277, 0.20889],      
    [0.69553, 0.54491, 0.21133],      
    [0.70287, 0.54703, 0.21396],      
    [0.7102, 0.54912, 0.2168],      
    [0.7175, 0.55117, 0.21984],      
    [0.72477, 0.55319, 0.22307],      
    [0.732, 0.55518, 0.22651],      
    [0.73921, 0.55716, 0.2301],      
    [0.74636, 0.55909, 0.23392],      
    [0.75347, 0.561, 0.23793],      
    [0.76053, 0.5629, 0.2421],      
    [0.76754, 0.56475, 0.24645],      
    [0.77449, 0.56661, 0.25099],      
    [0.78138, 0.56843, 0.25568],      
    [0.7882, 0.57024, 0.26055],      
    [0.79496, 0.57205, 0.26558],      
    [0.80164, 0.57383, 0.27078],      
    [0.80825, 0.57562, 0.27612],      
    [0.81478, 0.57739, 0.2816],      
    [0.82123, 0.57917, 0.28723],      
    [0.82759, 0.58094, 0.29301],      
    [0.83386, 0.58272, 0.29895],      
    [0.84004, 0.58451, 0.30501],      
    [0.84612, 0.5863, 0.3112],      
    [0.85211, 0.5881, 0.31753],      
    [0.85799, 0.58991, 0.32398],      
    [0.86378, 0.59175, 0.33055],      
    [0.86944, 0.5936, 0.33726],      
    [0.875, 0.59547, 0.34405],      
    [0.88044, 0.59737, 0.35099],      
    [0.88577, 0.59929, 0.35802],      
    [0.89097, 0.60122, 0.36514],      
    [0.89605, 0.6032, 0.37237],      
    [0.90099, 0.60519, 0.3797],      
    [0.90582, 0.60722, 0.38711],      
    [0.9105, 0.60928, 0.39462],      
    [0.91505, 0.61136, 0.40219],      
    [0.91946, 0.61347, 0.40986],      
    [0.92374, 0.61562, 0.41758],      
    [0.92787, 0.61779, 0.42536],      
    [0.93185, 0.62001, 0.4332],      
    [0.9357, 0.62223, 0.44109],      
    [0.9394, 0.6245, 0.44904],      
    [0.94295, 0.62679, 0.45701],      
    [0.94635, 0.62911, 0.46502],      
    [0.94962, 0.63145, 0.47305],      
    [0.95273, 0.63382, 0.48111],      
    [0.9557, 0.63621, 0.48918],      
    [0.95853, 0.63861, 0.49728],      
    [0.96121, 0.64103, 0.50536],      
    [0.96376, 0.64348, 0.51345],      
    [0.96616, 0.64594, 0.52153],      
    [0.96844, 0.64841, 0.52961],      
    [0.97058, 0.6509, 0.53767],      
    [0.97259, 0.6534, 0.54571],      
    [0.97447, 0.65591, 0.55373],      
    [0.97624, 0.65842, 0.56173],      
    [0.97788, 0.66093, 0.56969],      
    [0.97942, 0.66347, 0.57762],      
    [0.98084, 0.66599, 0.58554],      
    [0.98216, 0.66852, 0.5934],      
    [0.98337, 0.67105, 0.60124],      
    [0.98449, 0.67358, 0.60905],      
    [0.98551, 0.67611, 0.61681],      
    [0.98645, 0.67864, 0.62454],      
    [0.9873, 0.68116, 0.63223],      
    [0.98807, 0.68369, 0.6399],      
    [0.98877, 0.68622, 0.64752],      
    [0.9894, 0.68875, 0.65512],      
    [0.98996, 0.69126, 0.6627],      
    [0.99046, 0.69378, 0.67025],      
    [0.99089, 0.69631, 0.67777],      
    [0.99128, 0.69883, 0.68527],      
    [0.9916, 0.70135, 0.69277],      
    [0.99189, 0.70387, 0.70024],      
    [0.99212, 0.7064, 0.7077],      
    [0.99231, 0.70893, 0.71516],      
    [0.99246, 0.71146, 0.72262],      
    [0.99257, 0.71399, 0.73008],      
    [0.99265, 0.71654, 0.73754],      
    [0.99269, 0.71909, 0.74502],      
    [0.9927, 0.72164, 0.7525],      
    [0.99268, 0.7242, 0.76],      
    [0.99263, 0.72678, 0.76752],      
    [0.99255, 0.72936, 0.77506],      
    [0.99245, 0.73196, 0.78263],      
    [0.99232, 0.73456, 0.79022],      
    [0.99216, 0.73717, 0.79784],      
    [0.99199, 0.73981, 0.80549],      
    [0.99178, 0.74244, 0.81317],      
    [0.99156, 0.74509, 0.82089],      
    [0.99131, 0.74777, 0.82864],      
    [0.99104, 0.75044, 0.83642],      
    [0.99074, 0.75313, 0.84424],      
    [0.99043, 0.75584, 0.8521],      
    [0.99009, 0.75856, 0.85999],      
    [0.98972, 0.76129, 0.86791],      
    [0.98933, 0.76403, 0.87587],      
    [0.98892, 0.76678, 0.88386],      
    [0.98848, 0.76955, 0.89188],      
    [0.98802, 0.77232, 0.89993],      
    [0.98753, 0.77511, 0.908],      
    [0.98701, 0.77791, 0.9161],      
    [0.98647, 0.78071, 0.92423],      
    [0.98589, 0.78353, 0.93238],      
    [0.98529, 0.78635, 0.94056],      
    [0.98466, 0.78918, 0.94875],      
    [0.98399, 0.79201, 0.95696],      
    [0.98329, 0.79485, 0.96519],      
    [0.98257, 0.7977, 0.97344],      
    [0.9818, 0.80055, 0.98171]]            
# batlowK_cmap = LinearSegmentedColormap.from_list('batlowK', batlowK_cmdata)

mappy_rgb = numpy.array(batlowK_cmdata)
mappy_name = 'scientific colormaps 7 - batlowK'
fig = colormappy_figure(mappy_rgb, color_name=mappy_name)
fig = colormappy_attributes(mappy_rgb, color_name=mappy_name)
fig = scatter3D_Jpapbp(mappy_rgb, color_name=mappy_name)
fig = surface_sombrero(mappy_rgb, color_name=mappy_name)

plt.show()