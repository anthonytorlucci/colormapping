from sc7_context import colormappy

import matplotlib.pyplot as plt
import numpy

from colormappy_plotting import colormappy_figure, colormappy_attributes, scatter3D_Jpapbp, surface_sombrero

lapaz_cmdata = [
    [0.10352, 0.047787, 0.39353],      
    [0.10489, 0.053521, 0.39674],      
    [0.10638, 0.059148, 0.39996],      
    [0.10772, 0.064483, 0.40319],      
    [0.1091, 0.06976, 0.4064],      
    [0.11045, 0.074827, 0.40961],      
    [0.11175, 0.079829, 0.41283],      
    [0.11305, 0.084796, 0.41603],      
    [0.11424, 0.089643, 0.41924],      
    [0.11551, 0.094446, 0.42243],      
    [0.11673, 0.099126, 0.42564],      
    [0.11793, 0.10381, 0.42883],      
    [0.11911, 0.10838, 0.43203],      
    [0.12024, 0.11303, 0.4352],      
    [0.12136, 0.11751, 0.43837],      
    [0.12248, 0.12198, 0.44154],      
    [0.12359, 0.12648, 0.4447],      
    [0.1247, 0.13094, 0.44784],      
    [0.12581, 0.13532, 0.45099],      
    [0.12683, 0.13967, 0.45412],      
    [0.12791, 0.14407, 0.45724],      
    [0.12892, 0.14838, 0.46034],      
    [0.12999, 0.1527, 0.46344],      
    [0.13099, 0.15701, 0.46653],      
    [0.13199, 0.16132, 0.46961],      
    [0.13298, 0.16553, 0.47266],      
    [0.13398, 0.16983, 0.47572],      
    [0.13497, 0.17405, 0.47874],      
    [0.13589, 0.17829, 0.48176],      
    [0.13689, 0.18246, 0.48476],      
    [0.13789, 0.18667, 0.48776],      
    [0.13882, 0.19085, 0.49073],      
    [0.13975, 0.19504, 0.49367],      
    [0.14077, 0.19918, 0.4966],      
    [0.14171, 0.20336, 0.49951],      
    [0.14266, 0.20751, 0.50242],      
    [0.14363, 0.21165, 0.50529],      
    [0.14459, 0.21578, 0.50816],      
    [0.14558, 0.21989, 0.51099],      
    [0.1465, 0.22398, 0.51382],      
    [0.14749, 0.22811, 0.51661],      
    [0.14844, 0.2322, 0.51939],      
    [0.14946, 0.23628, 0.52213],      
    [0.15044, 0.24033, 0.52487],      
    [0.15142, 0.2444, 0.52758],      
    [0.15243, 0.24849, 0.53026],      
    [0.15344, 0.25253, 0.53293],      
    [0.15448, 0.25657, 0.53556],      
    [0.15554, 0.26061, 0.53818],      
    [0.1566, 0.26464, 0.54076],      
    [0.15765, 0.26868, 0.54333],      
    [0.15876, 0.27268, 0.54587],      
    [0.15981, 0.2767, 0.54838],      
    [0.16096, 0.28068, 0.55086],      
    [0.16211, 0.28467, 0.55332],      
    [0.16326, 0.28867, 0.55574],      
    [0.16443, 0.29264, 0.55815],      
    [0.16559, 0.29662, 0.56053],      
    [0.16684, 0.30057, 0.56289],      
    [0.16805, 0.30453, 0.56519],      
    [0.16935, 0.30849, 0.5675],      
    [0.17061, 0.31241, 0.56975],      
    [0.17192, 0.31636, 0.57199],      
    [0.17326, 0.32029, 0.57419],      
    [0.17465, 0.32419, 0.57638],      
    [0.17601, 0.3281, 0.57851],      
    [0.17748, 0.33201, 0.58063],      
    [0.17892, 0.3359, 0.5827],      
    [0.18039, 0.33979, 0.58476],      
    [0.18191, 0.34365, 0.58678],      
    [0.18348, 0.34753, 0.58876],      
    [0.18509, 0.35138, 0.59073],      
    [0.1867, 0.35524, 0.59266],      
    [0.18839, 0.35907, 0.59455],      
    [0.19007, 0.3629, 0.59641],      
    [0.19181, 0.36673, 0.59824],      
    [0.19361, 0.37054, 0.60004],      
    [0.19542, 0.37436, 0.6018],      
    [0.1973, 0.37814, 0.60353],      
    [0.19919, 0.38193, 0.60522],      
    [0.20114, 0.3857, 0.60689],      
    [0.20317, 0.38948, 0.60852],      
    [0.20521, 0.39324, 0.6101],      
    [0.20732, 0.39698, 0.61166],      
    [0.20945, 0.40074, 0.61318],      
    [0.21167, 0.40445, 0.61467],      
    [0.2139, 0.40817, 0.61612],      
    [0.21621, 0.41188, 0.61754],      
    [0.21855, 0.41558, 0.61892],      
    [0.22096, 0.41927, 0.62026],      
    [0.22341, 0.42293, 0.62156],      
    [0.22593, 0.4266, 0.62283],      
    [0.2285, 0.43025, 0.62407],      
    [0.23111, 0.43388, 0.62525],      
    [0.23377, 0.43753, 0.62641],      
    [0.23654, 0.44113, 0.62752],      
    [0.23932, 0.44474, 0.6286],      
    [0.24218, 0.44832, 0.62963],      
    [0.24508, 0.4519, 0.63064],      
    [0.24809, 0.45546, 0.63159],      
    [0.25112, 0.459, 0.6325],      
    [0.25422, 0.46252, 0.63338],      
    [0.25738, 0.46604, 0.63421],      
    [0.2606, 0.46955, 0.635],      
    [0.2639, 0.47302, 0.63575],      
    [0.26722, 0.47649, 0.63646],      
    [0.27066, 0.47994, 0.63712],      
    [0.27412, 0.48336, 0.63774],      
    [0.27766, 0.48677, 0.63831],      
    [0.28125, 0.49016, 0.63885],      
    [0.28491, 0.49353, 0.63933],      
    [0.28864, 0.49688, 0.63978],      
    [0.29243, 0.5002, 0.64018],      
    [0.29628, 0.50351, 0.64052],      
    [0.30018, 0.50679, 0.64083],      
    [0.30415, 0.51005, 0.64108],      
    [0.30818, 0.51329, 0.6413],      
    [0.31225, 0.51649, 0.64146],      
    [0.31642, 0.51968, 0.64158],      
    [0.32063, 0.52284, 0.64165],      
    [0.32486, 0.52597, 0.64168],      
    [0.3292, 0.52907, 0.64166],      
    [0.33356, 0.53214, 0.64158],      
    [0.33797, 0.53517, 0.64147],      
    [0.34246, 0.53819, 0.6413],      
    [0.34698, 0.54115, 0.64109],      
    [0.35154, 0.5441, 0.64083],      
    [0.35617, 0.54701, 0.64052],      
    [0.36082, 0.54989, 0.64017],      
    [0.36554, 0.55273, 0.63977],      
    [0.37029, 0.55553, 0.63932],      
    [0.37509, 0.5583, 0.63882],      
    [0.37993, 0.56104, 0.63828],      
    [0.3848, 0.56374, 0.6377],      
    [0.38971, 0.56639, 0.63707],      
    [0.39466, 0.569, 0.6364],      
    [0.39963, 0.57158, 0.63567],      
    [0.40464, 0.57411, 0.63491],      
    [0.4097, 0.57662, 0.63412],      
    [0.41476, 0.57907, 0.63327],      
    [0.41986, 0.58148, 0.63238],      
    [0.42498, 0.58386, 0.63146],      
    [0.43012, 0.58619, 0.63051],      
    [0.43529, 0.58847, 0.6295],      
    [0.44047, 0.59072, 0.62848],      
    [0.44567, 0.59294, 0.62741],      
    [0.4509, 0.5951, 0.62631],      
    [0.45613, 0.59723, 0.62518],      
    [0.46139, 0.59931, 0.62402],      
    [0.46666, 0.60135, 0.62283],      
    [0.47194, 0.60335, 0.62161],      
    [0.47722, 0.60531, 0.62039],      
    [0.48252, 0.60725, 0.61913],      
    [0.48784, 0.60914, 0.61784],      
    [0.49315, 0.61099, 0.61655],      
    [0.49849, 0.61279, 0.61523],      
    [0.50382, 0.61458, 0.6139],      
    [0.50917, 0.61633, 0.61257],      
    [0.51452, 0.61805, 0.61123],      
    [0.51987, 0.61974, 0.60988],      
    [0.52524, 0.6214, 0.60853],      
    [0.53062, 0.62303, 0.60718],      
    [0.536, 0.62464, 0.60582],      
    [0.54139, 0.62623, 0.60448],      
    [0.54681, 0.6278, 0.60314],      
    [0.55222, 0.62935, 0.60182],      
    [0.55765, 0.63089, 0.60051],      
    [0.56309, 0.63241, 0.59923],      
    [0.56854, 0.63393, 0.59796],      
    [0.57402, 0.63543, 0.59673],      
    [0.57952, 0.63694, 0.59553],      
    [0.58503, 0.63844, 0.59436],      
    [0.59056, 0.63995, 0.59324],      
    [0.59612, 0.64146, 0.59217],      
    [0.6017, 0.64299, 0.59114],      
    [0.60733, 0.64453, 0.59016],      
    [0.61297, 0.64609, 0.58925],      
    [0.61866, 0.64767, 0.58841],      
    [0.62438, 0.64929, 0.58765],      
    [0.63014, 0.65093, 0.58696],      
    [0.63594, 0.6526, 0.58636],      
    [0.64179, 0.65432, 0.58586],      
    [0.64769, 0.6561, 0.58545],      
    [0.65365, 0.65791, 0.58514],      
    [0.65966, 0.65978, 0.58495],      
    [0.66573, 0.66172, 0.58488],      
    [0.67185, 0.66373, 0.58495],      
    [0.67805, 0.6658, 0.58515],      
    [0.6843, 0.66795, 0.58549],      
    [0.69062, 0.67019, 0.58599],      
    [0.69702, 0.67251, 0.58664],      
    [0.70348, 0.67492, 0.58747],      
    [0.71002, 0.67743, 0.58847],      
    [0.71662, 0.68003, 0.58967],      
    [0.72329, 0.68276, 0.59106],      
    [0.73003, 0.68559, 0.59265],      
    [0.73684, 0.68853, 0.59444],      
    [0.74371, 0.69159, 0.59646],      
    [0.75064, 0.69476, 0.59869],      
    [0.75762, 0.69806, 0.60115],      
    [0.76465, 0.70148, 0.60385],      
    [0.77173, 0.70503, 0.60677],      
    [0.77884, 0.70871, 0.60994],      
    [0.78598, 0.71249, 0.61334],      
    [0.79313, 0.71641, 0.617],      
    [0.80029, 0.72043, 0.62089],      
    [0.80745, 0.72458, 0.62501],      
    [0.81459, 0.72884, 0.62938],      
    [0.82171, 0.73321, 0.63398],      
    [0.82878, 0.73767, 0.6388],      
    [0.8358, 0.74224, 0.64385],      
    [0.84275, 0.74689, 0.64912],      
    [0.84963, 0.75162, 0.65458],      
    [0.8564, 0.75642, 0.66025],      
    [0.86308, 0.76129, 0.6661],      
    [0.86964, 0.76622, 0.67213],      
    [0.87606, 0.7712, 0.67832],      
    [0.88235, 0.77622, 0.68466],      
    [0.88848, 0.78127, 0.69113],      
    [0.89445, 0.78634, 0.69774],      
    [0.90025, 0.79142, 0.70446],      
    [0.90588, 0.79651, 0.71129],      
    [0.91132, 0.80161, 0.7182],      
    [0.91657, 0.8067, 0.72519],      
    [0.92163, 0.81176, 0.73224],      
    [0.92649, 0.81681, 0.73935],      
    [0.93115, 0.82184, 0.7465],      
    [0.93562, 0.82683, 0.75368],      
    [0.93989, 0.83179, 0.7609],      
    [0.94396, 0.83671, 0.76812],      
    [0.94784, 0.84159, 0.77536],      
    [0.95153, 0.84642, 0.78261],      
    [0.95503, 0.8512, 0.78985],      
    [0.95835, 0.85595, 0.79708],      
    [0.96148, 0.86064, 0.80431],      
    [0.96444, 0.86528, 0.81152],      
    [0.96724, 0.86987, 0.8187],      
    [0.96988, 0.87442, 0.82587],      
    [0.97236, 0.87892, 0.83302],      
    [0.97468, 0.88337, 0.84014],      
    [0.97687, 0.88777, 0.84724],      
    [0.97893, 0.89214, 0.85431],      
    [0.98085, 0.89646, 0.86136],      
    [0.98265, 0.90074, 0.86839],      
    [0.98434, 0.90498, 0.87538],      
    [0.98591, 0.90918, 0.88236],      
    [0.98739, 0.91335, 0.88932],      
    [0.98876, 0.9175, 0.89625],      
    [0.99005, 0.92161, 0.90317],      
    [0.99126, 0.92569, 0.91007],      
    [0.99239, 0.92975, 0.91695],      
    [0.99344, 0.93379, 0.92382],      
    [0.99443, 0.93782, 0.93068],      
    [0.99536, 0.94182, 0.93753],      
    [0.99624, 0.94581, 0.94437],      
    [0.99706, 0.94979, 0.95121]]            
# lapaz_cmap = LinearSegmentedColormap.from_list('lapaz', lapaz_cmdata)

mappy_rgb = numpy.array(lapaz_cmdata)
mappy_name = 'scientific colormaps 7 - lapaz'
fig = colormappy_figure(mappy_rgb, color_name=mappy_name)
fig = colormappy_attributes(mappy_rgb, color_name=mappy_name)
fig = scatter3D_Jpapbp(mappy_rgb, color_name=mappy_name)
fig = surface_sombrero(mappy_rgb, color_name=mappy_name)

plt.show()