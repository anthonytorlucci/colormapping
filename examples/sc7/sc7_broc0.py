from sc7_context import colormappy

import matplotlib.pyplot as plt
import numpy

from colormappy_plotting import colormappy_figure, colormappy_attributes, scatter3D_Jpapbp, surface_sombrero

broc0_cmdata = [
    [0.21429, 0.18467, 0.21821],      
    [0.21369, 0.18469, 0.22245],      
    [0.21315, 0.18487, 0.22685],      
    [0.21268, 0.18522, 0.23141],      
    [0.21227, 0.18574, 0.23612],      
    [0.21191, 0.1864, 0.24097],      
    [0.21159, 0.18728, 0.24599],      
    [0.21131, 0.18833, 0.2512],      
    [0.21109, 0.18953, 0.25653],      
    [0.21092, 0.19094, 0.26205],      
    [0.21081, 0.19255, 0.2677],      
    [0.21075, 0.19438, 0.27356],      
    [0.21074, 0.19638, 0.27955],      
    [0.21078, 0.19855, 0.28568],      
    [0.21088, 0.20094, 0.292],      
    [0.21104, 0.20358, 0.29845],      
    [0.21126, 0.20641, 0.30507],      
    [0.21155, 0.2094, 0.31181],      
    [0.2119, 0.21264, 0.31871],      
    [0.21232, 0.2161, 0.32573],      
    [0.21279, 0.21973, 0.33291],      
    [0.21336, 0.22357, 0.34018],      
    [0.21404, 0.22763, 0.34757],      
    [0.21477, 0.23189, 0.35506],      
    [0.21563, 0.23634, 0.36263],      
    [0.2166, 0.24096, 0.3703],      
    [0.21764, 0.24579, 0.37804],      
    [0.21882, 0.25081, 0.38584],      
    [0.22014, 0.25598, 0.3937],      
    [0.22156, 0.26135, 0.4016],      
    [0.22314, 0.26685, 0.40953],      
    [0.22483, 0.27251, 0.41748],      
    [0.22674, 0.27834, 0.42543],      
    [0.22878, 0.28428, 0.43337],      
    [0.23097, 0.29035, 0.44131],      
    [0.23333, 0.29656, 0.44923],      
    [0.23591, 0.30285, 0.45709],      
    [0.23863, 0.30929, 0.46493],      
    [0.24157, 0.31579, 0.4727],      
    [0.24466, 0.32237, 0.48043],      
    [0.248, 0.32904, 0.48809],      
    [0.2515, 0.33577, 0.49566],      
    [0.2552, 0.34257, 0.50316],      
    [0.25909, 0.34941, 0.51059],      
    [0.26316, 0.35631, 0.51793],      
    [0.26741, 0.36324, 0.52517],      
    [0.27187, 0.37021, 0.53232],      
    [0.27655, 0.37723, 0.53937],      
    [0.28136, 0.38425, 0.54634],      
    [0.28636, 0.3913, 0.5532],      
    [0.29157, 0.39836, 0.55997],      
    [0.29692, 0.40544, 0.56664],      
    [0.30241, 0.41252, 0.57321],      
    [0.30809, 0.41961, 0.5797],      
    [0.31393, 0.42669, 0.58608],      
    [0.3199, 0.43377, 0.59238],      
    [0.326, 0.44085, 0.59857],      
    [0.33227, 0.44793, 0.60469],      
    [0.33864, 0.45502, 0.61072],      
    [0.34514, 0.46207, 0.61667],      
    [0.35176, 0.46913, 0.62253],      
    [0.35849, 0.47617, 0.62832],      
    [0.36534, 0.4832, 0.63403],      
    [0.37228, 0.49022, 0.63967],      
    [0.37933, 0.49723, 0.64523],      
    [0.38646, 0.50423, 0.65073],      
    [0.3937, 0.5112, 0.65616],      
    [0.40102, 0.51817, 0.66152],      
    [0.4084, 0.52512, 0.66681],      
    [0.41586, 0.53206, 0.67206],      
    [0.42339, 0.53898, 0.67724],      
    [0.43101, 0.54589, 0.68235],      
    [0.43866, 0.55277, 0.68742],      
    [0.44639, 0.55965, 0.69243],      
    [0.45418, 0.56651, 0.69737],      
    [0.462, 0.57335, 0.70227],      
    [0.46989, 0.58017, 0.70711],      
    [0.47781, 0.58697, 0.71189],      
    [0.48577, 0.59376, 0.71662],      
    [0.49378, 0.60052, 0.72128],      
    [0.50183, 0.60728, 0.72589],      
    [0.50989, 0.61399, 0.73044],      
    [0.518, 0.6207, 0.73493],      
    [0.52612, 0.62737, 0.73936],      
    [0.53426, 0.63403, 0.74372],      
    [0.54243, 0.64065, 0.74801],      
    [0.5506, 0.64725, 0.75222],      
    [0.55878, 0.65382, 0.75637],      
    [0.56698, 0.66035, 0.76043],      
    [0.57517, 0.66685, 0.76441],      
    [0.58335, 0.67331, 0.76829],      
    [0.59154, 0.67972, 0.77209],      
    [0.59971, 0.6861, 0.77579],      
    [0.60786, 0.69243, 0.77938],      
    [0.61598, 0.6987, 0.78285],      
    [0.62408, 0.70491, 0.78621],      
    [0.63214, 0.71107, 0.78944],      
    [0.64016, 0.71716, 0.79253],      
    [0.64812, 0.72317, 0.79548],      
    [0.65605, 0.72911, 0.79828],      
    [0.66389, 0.73497, 0.80092],      
    [0.67166, 0.74072, 0.80338],      
    [0.67935, 0.74639, 0.80566],      
    [0.68695, 0.75195, 0.80776],      
    [0.69444, 0.75739, 0.80965],      
    [0.70182, 0.76271, 0.81133],      
    [0.70908, 0.7679, 0.81279],      
    [0.7162, 0.77295, 0.81401],      
    [0.72317, 0.77786, 0.81499],      
    [0.72999, 0.7826, 0.81572],      
    [0.73662, 0.78717, 0.81619],      
    [0.74307, 0.79156, 0.81637],      
    [0.74931, 0.79576, 0.81627],      
    [0.75536, 0.79977, 0.81588],      
    [0.76116, 0.80355, 0.81518],      
    [0.76672, 0.80712, 0.81417],      
    [0.77203, 0.81045, 0.81284],      
    [0.77708, 0.81354, 0.8112],      
    [0.78184, 0.81639, 0.80922],      
    [0.7863, 0.81896, 0.80691],      
    [0.79045, 0.82127, 0.80426],      
    [0.79429, 0.8233, 0.80127],      
    [0.7978, 0.82504, 0.79794],      
    [0.80098, 0.8265, 0.79428],      
    [0.8038, 0.82765, 0.79028],      
    [0.80628, 0.82851, 0.78595],      
    [0.80839, 0.82906, 0.78129],      
    [0.81014, 0.82929, 0.77631],      
    [0.81153, 0.82922, 0.77101],      
    [0.81253, 0.82883, 0.76541],      
    [0.81317, 0.82813, 0.7595],      
    [0.81344, 0.82712, 0.75332],      
    [0.81334, 0.8258, 0.74687],      
    [0.81288, 0.82418, 0.74015],      
    [0.81205, 0.82226, 0.73317],      
    [0.81087, 0.82004, 0.72597],      
    [0.80934, 0.81753, 0.71853],      
    [0.80746, 0.81474, 0.7109],      
    [0.80524, 0.81167, 0.70307],      
    [0.80271, 0.80833, 0.69506],      
    [0.79986, 0.80473, 0.68688],      
    [0.79669, 0.80088, 0.67856],      
    [0.79324, 0.79678, 0.6701],      
    [0.7895, 0.79245, 0.66152],      
    [0.78548, 0.7879, 0.65283],      
    [0.78121, 0.78312, 0.64404],      
    [0.77669, 0.77815, 0.63518],      
    [0.77192, 0.77297, 0.62625],      
    [0.76693, 0.76761, 0.61726],      
    [0.76173, 0.76207, 0.60824],      
    [0.75633, 0.75636, 0.59917],      
    [0.75074, 0.7505, 0.59007],      
    [0.74495, 0.74448, 0.58097],      
    [0.73902, 0.73832, 0.57187],      
    [0.73291, 0.73203, 0.56278],      
    [0.72666, 0.72562, 0.55368],      
    [0.72027, 0.71908, 0.54462],      
    [0.71376, 0.71244, 0.53558],      
    [0.70713, 0.7057, 0.5266],      
    [0.70038, 0.69887, 0.51764],      
    [0.69354, 0.69195, 0.50874],      
    [0.68661, 0.68495, 0.49988],      
    [0.67959, 0.67789, 0.49111],      
    [0.67251, 0.67075, 0.48238],      
    [0.66534, 0.66356, 0.47371],      
    [0.65813, 0.65631, 0.46513],      
    [0.65085, 0.64901, 0.45663],      
    [0.64352, 0.64166, 0.44821],      
    [0.63617, 0.63429, 0.43988],      
    [0.62877, 0.62688, 0.43163],      
    [0.62134, 0.61944, 0.42345],      
    [0.61388, 0.61197, 0.41538],      
    [0.60642, 0.6045, 0.40741],      
    [0.59893, 0.597, 0.39952],      
    [0.59144, 0.58948, 0.39174],      
    [0.58394, 0.58196, 0.38405],      
    [0.57645, 0.57444, 0.37648],      
    [0.56894, 0.56693, 0.36899],      
    [0.56146, 0.5594, 0.36161],      
    [0.55398, 0.55189, 0.35433],      
    [0.54652, 0.54437, 0.34717],      
    [0.53906, 0.53688, 0.3401],      
    [0.53164, 0.52939, 0.33314],      
    [0.52423, 0.52191, 0.32627],      
    [0.51686, 0.51447, 0.31955],      
    [0.50951, 0.50703, 0.31291],      
    [0.5022, 0.49962, 0.30641],      
    [0.49493, 0.49224, 0.29999],      
    [0.48769, 0.48488, 0.29369],      
    [0.48049, 0.47755, 0.28752],      
    [0.47333, 0.47026, 0.28147],      
    [0.46623, 0.46299, 0.27555],      
    [0.45918, 0.45577, 0.26973],      
    [0.45218, 0.44859, 0.26404],      
    [0.44523, 0.44144, 0.25845],      
    [0.43834, 0.43433, 0.25302],      
    [0.43152, 0.42729, 0.24771],      
    [0.42476, 0.42027, 0.24251],      
    [0.41806, 0.41332, 0.2375],      
    [0.41144, 0.40641, 0.23256],      
    [0.40488, 0.39955, 0.2278],      
    [0.39842, 0.39277, 0.22317],      
    [0.39203, 0.38603, 0.21868],      
    [0.38571, 0.37938, 0.21434],      
    [0.3795, 0.37278, 0.21015],      
    [0.37337, 0.36627, 0.20613],      
    [0.36733, 0.35981, 0.20222],      
    [0.3614, 0.35344, 0.19849],      
    [0.35557, 0.34715, 0.19495],      
    [0.34983, 0.34094, 0.19153],      
    [0.34418, 0.33483, 0.18832],      
    [0.33867, 0.32879, 0.18525],      
    [0.33328, 0.32285, 0.18231],      
    [0.32797, 0.317, 0.17959],      
    [0.32281, 0.31126, 0.17704],      
    [0.31775, 0.30563, 0.17466],      
    [0.31281, 0.30008, 0.17243],      
    [0.308, 0.29465, 0.1704],      
    [0.30332, 0.28935, 0.16854],      
    [0.29879, 0.28414, 0.16687],      
    [0.29436, 0.27908, 0.16532],      
    [0.29007, 0.27411, 0.16403],      
    [0.28591, 0.26928, 0.16286],      
    [0.28191, 0.26455, 0.16189],      
    [0.27802, 0.25997, 0.16107],      
    [0.27426, 0.25551, 0.16039],      
    [0.27065, 0.25118, 0.15992],      
    [0.26713, 0.24697, 0.15963],      
    [0.2638, 0.24289, 0.1595],      
    [0.26056, 0.23896, 0.15954],      
    [0.25747, 0.23519, 0.15973],      
    [0.25451, 0.23152, 0.16009],      
    [0.25167, 0.22798, 0.16064],      
    [0.24895, 0.22455, 0.16136],      
    [0.24634, 0.22132, 0.16219],      
    [0.24386, 0.2182, 0.16319],      
    [0.24152, 0.2152, 0.16434],      
    [0.23927, 0.21237, 0.1656],      
    [0.23716, 0.20964, 0.1671],      
    [0.23513, 0.20708, 0.16869],      
    [0.23318, 0.20464, 0.17044],      
    [0.23139, 0.20231, 0.17233],      
    [0.22964, 0.20014, 0.17439],      
    [0.22805, 0.19812, 0.17655],      
    [0.22652, 0.19626, 0.17891],      
    [0.22505, 0.19452, 0.18136],      
    [0.22371, 0.19288, 0.18399],      
    [0.22244, 0.1914, 0.18676],      
    [0.22126, 0.19007, 0.18967],      
    [0.22015, 0.18889, 0.19273],      
    [0.21911, 0.18786, 0.19593],      
    [0.21814, 0.18693, 0.19925],      
    [0.21724, 0.18619, 0.20275],      
    [0.21642, 0.1856, 0.20642],      
    [0.21564, 0.18513, 0.21018],      
    [0.21492, 0.18482, 0.21413]]            
# brocO_cmap = LinearSegmentedColormap.from_list('brocO', broc0_cmdata)

mappy_rgb = numpy.array(broc0_cmdata)
mappy_name = 'scientific colormaps 7 - broc0'
fig = colormappy_figure(mappy_rgb, color_name=mappy_name)
fig = colormappy_attributes(mappy_rgb, color_name=mappy_name)
fig = scatter3D_Jpapbp(mappy_rgb, color_name=mappy_name)
fig = surface_sombrero(mappy_rgb, color_name=mappy_name)

plt.show()