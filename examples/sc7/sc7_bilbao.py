from sc7_context import colormappy

import matplotlib.pyplot as plt
import numpy

from colormappy_plotting import colormappy_figure, colormappy_attributes, scatter3D_Jpapbp, surface_sombrero

bilbao_cmdata = [
    [1, 1, 0.99991],      
    [0.99488, 0.99486, 0.99473],      
    [0.98976, 0.98973, 0.98957],      
    [0.98465, 0.9846, 0.98439],      
    [0.97954, 0.97948, 0.97922],      
    [0.97444, 0.97436, 0.97404],      
    [0.96934, 0.96925, 0.96886],      
    [0.96426, 0.96414, 0.96368],      
    [0.95919, 0.95905, 0.95849],      
    [0.95413, 0.95395, 0.95329],      
    [0.94907, 0.94887, 0.94808],      
    [0.94404, 0.94379, 0.94287],      
    [0.93901, 0.93872, 0.93764],      
    [0.93399, 0.93366, 0.93239],      
    [0.929, 0.92861, 0.92713],      
    [0.92403, 0.92357, 0.92186],      
    [0.91907, 0.91854, 0.91656],      
    [0.91414, 0.91353, 0.91124],      
    [0.90923, 0.90853, 0.9059],      
    [0.90435, 0.90354, 0.90053],      
    [0.8995, 0.89857, 0.89514],      
    [0.89469, 0.89362, 0.88971],      
    [0.8899, 0.8887, 0.88426],      
    [0.88516, 0.88381, 0.87878],      
    [0.88046, 0.87893, 0.87327],      
    [0.87582, 0.87409, 0.86773],      
    [0.87122, 0.86929, 0.86216],      
    [0.86668, 0.86453, 0.85655],      
    [0.86221, 0.8598, 0.85092],      
    [0.8578, 0.85513, 0.84526],      
    [0.85346, 0.8505, 0.83958],      
    [0.8492, 0.84592, 0.83387],      
    [0.84501, 0.84141, 0.82813],      
    [0.84091, 0.83696, 0.82239],      
    [0.8369, 0.83257, 0.81662],      
    [0.83298, 0.82826, 0.81084],      
    [0.82916, 0.82402, 0.80506],      
    [0.82543, 0.81985, 0.79928],      
    [0.82181, 0.81578, 0.79349],      
    [0.81829, 0.81178, 0.7877],      
    [0.81487, 0.80786, 0.78193],      
    [0.81157, 0.80403, 0.77616],      
    [0.80836, 0.80029, 0.77041],      
    [0.80526, 0.79664, 0.76468],      
    [0.80227, 0.79308, 0.75897],      
    [0.79938, 0.7896, 0.75329],      
    [0.79658, 0.78622, 0.74764],      
    [0.7939, 0.78291, 0.74201],      
    [0.7913, 0.77969, 0.73641],      
    [0.7888, 0.77656, 0.73085],      
    [0.78639, 0.77349, 0.72533],      
    [0.78406, 0.77051, 0.71983],      
    [0.78181, 0.76759, 0.71436],      
    [0.77963, 0.76475, 0.70894],      
    [0.77754, 0.76196, 0.70353],      
    [0.77549, 0.75924, 0.69816],      
    [0.77352, 0.75658, 0.69284],      
    [0.77161, 0.75396, 0.68752],      
    [0.76974, 0.7514, 0.68224],      
    [0.76792, 0.74887, 0.677],      
    [0.76616, 0.74638, 0.67176],      
    [0.76442, 0.74393, 0.66655],      
    [0.76272, 0.74151, 0.66137],      
    [0.76106, 0.73912, 0.6562],      
    [0.75942, 0.73674, 0.65105],      
    [0.75781, 0.73439, 0.6459],      
    [0.75622, 0.73205, 0.64078],      
    [0.75465, 0.72972, 0.63566],      
    [0.75309, 0.72739, 0.63056],      
    [0.75155, 0.72508, 0.62545],      
    [0.75001, 0.72275, 0.62036],      
    [0.74849, 0.72042, 0.61525],      
    [0.74696, 0.71808, 0.61016],      
    [0.74544, 0.71573, 0.60506],      
    [0.74393, 0.71336, 0.59996],      
    [0.74241, 0.71097, 0.59485],      
    [0.74088, 0.70854, 0.58974],      
    [0.73937, 0.70609, 0.58462],      
    [0.73783, 0.70359, 0.5795],      
    [0.73628, 0.70106, 0.57435],      
    [0.73474, 0.69848, 0.56921],      
    [0.73318, 0.69585, 0.56406],      
    [0.73161, 0.69316, 0.55889],      
    [0.73002, 0.69041, 0.55373],      
    [0.72842, 0.68759, 0.54857],      
    [0.72681, 0.68471, 0.54339],      
    [0.72519, 0.68175, 0.53823],      
    [0.72354, 0.67872, 0.53307],      
    [0.72189, 0.67561, 0.52792],      
    [0.72023, 0.67242, 0.5228],      
    [0.71855, 0.66915, 0.5177],      
    [0.71687, 0.6658, 0.51263],      
    [0.71517, 0.66238, 0.50762],      
    [0.71347, 0.65887, 0.50265],      
    [0.71176, 0.65529, 0.49776],      
    [0.71006, 0.65165, 0.49292],      
    [0.70836, 0.64793, 0.48819],      
    [0.70666, 0.64416, 0.48353],      
    [0.70497, 0.64035, 0.47899],      
    [0.7033, 0.63649, 0.47457],      
    [0.70163, 0.63258, 0.47026],      
    [0.69999, 0.62865, 0.46606],      
    [0.69837, 0.62469, 0.46202],      
    [0.69678, 0.62072, 0.45811],      
    [0.69521, 0.61674, 0.45435],      
    [0.69366, 0.61275, 0.45072],      
    [0.69216, 0.60879, 0.44723],      
    [0.69067, 0.60481, 0.44391],      
    [0.68923, 0.60086, 0.4407],      
    [0.68781, 0.59693, 0.43766],      
    [0.68642, 0.59303, 0.43474],      
    [0.68507, 0.58913, 0.43195],      
    [0.68375, 0.58529, 0.42927],      
    [0.68245, 0.58145, 0.42672],      
    [0.68119, 0.57766, 0.42428],      
    [0.67995, 0.57389, 0.42194],      
    [0.67875, 0.57015, 0.41971],      
    [0.67757, 0.56645, 0.41755],      
    [0.6764, 0.56277, 0.41547],      
    [0.67526, 0.5591, 0.41347],      
    [0.67413, 0.55547, 0.41153],      
    [0.67303, 0.55187, 0.40966],      
    [0.67194, 0.54828, 0.40784],      
    [0.67087, 0.54471, 0.40607],      
    [0.66981, 0.54115, 0.40433],      
    [0.66875, 0.53763, 0.40263],      
    [0.66771, 0.5341, 0.40098],      
    [0.66667, 0.5306, 0.39933],      
    [0.66565, 0.52711, 0.39773],      
    [0.66463, 0.52362, 0.39614],      
    [0.66363, 0.52013, 0.39457],      
    [0.66262, 0.51667, 0.39301],      
    [0.66162, 0.51321, 0.39148],      
    [0.66061, 0.50975, 0.38994],      
    [0.65962, 0.5063, 0.38843],      
    [0.65862, 0.50285, 0.38691],      
    [0.65764, 0.49941, 0.3854],      
    [0.65664, 0.49597, 0.38391],      
    [0.65565, 0.49253, 0.38241],      
    [0.65466, 0.48909, 0.38093],      
    [0.65368, 0.48566, 0.37943],      
    [0.65269, 0.48223, 0.37795],      
    [0.65171, 0.4788, 0.37647],      
    [0.65072, 0.47537, 0.37498],      
    [0.64973, 0.47194, 0.3735],      
    [0.64874, 0.4685, 0.37201],      
    [0.64775, 0.46507, 0.37052],      
    [0.64676, 0.46164, 0.36905],      
    [0.64577, 0.4582, 0.36755],      
    [0.64477, 0.45477, 0.36607],      
    [0.64377, 0.45132, 0.36457],      
    [0.64278, 0.44787, 0.36307],      
    [0.64177, 0.44444, 0.36158],      
    [0.64076, 0.44098, 0.36007],      
    [0.63975, 0.43754, 0.35856],      
    [0.63872, 0.43406, 0.35706],      
    [0.6377, 0.43061, 0.35554],      
    [0.63666, 0.42714, 0.35399],      
    [0.63561, 0.42365, 0.35245],      
    [0.63455, 0.42016, 0.35091],      
    [0.63348, 0.41667, 0.34933],      
    [0.63239, 0.41316, 0.34776],      
    [0.63128, 0.40964, 0.34615],      
    [0.63016, 0.40611, 0.34453],      
    [0.62901, 0.40254, 0.34291],      
    [0.62784, 0.39898, 0.34125],      
    [0.62664, 0.3954, 0.33957],      
    [0.62542, 0.3918, 0.33784],      
    [0.62416, 0.38817, 0.33609],      
    [0.62286, 0.38452, 0.33433],      
    [0.62152, 0.38085, 0.33251],      
    [0.62015, 0.37715, 0.33064],      
    [0.61872, 0.37341, 0.32874],      
    [0.61724, 0.36965, 0.32678],      
    [0.6157, 0.36586, 0.32478],      
    [0.6141, 0.36204, 0.32274],      
    [0.61245, 0.35818, 0.32062],      
    [0.61073, 0.35427, 0.31843],      
    [0.60893, 0.35035, 0.31619],      
    [0.60706, 0.34636, 0.31388],      
    [0.6051, 0.34235, 0.31148],      
    [0.60307, 0.33829, 0.30904],      
    [0.60095, 0.33421, 0.3065],      
    [0.59874, 0.33007, 0.30386],      
    [0.59644, 0.32588, 0.30116],      
    [0.59405, 0.32167, 0.29838],      
    [0.59156, 0.31742, 0.29552],      
    [0.58897, 0.31313, 0.29257],      
    [0.5863, 0.30882, 0.28955],      
    [0.58352, 0.30445, 0.28641],      
    [0.58065, 0.30006, 0.28323],      
    [0.57768, 0.29564, 0.27994],      
    [0.57462, 0.29121, 0.27658],      
    [0.57147, 0.28673, 0.27314],      
    [0.56822, 0.28227, 0.26963],      
    [0.56489, 0.27776, 0.26603],      
    [0.56148, 0.27324, 0.26236],      
    [0.55798, 0.26872, 0.25864],      
    [0.55441, 0.26418, 0.25486],      
    [0.55076, 0.25964, 0.251],      
    [0.54704, 0.2551, 0.24709],      
    [0.54326, 0.25053, 0.24312],      
    [0.53941, 0.24598, 0.23913],      
    [0.5355, 0.24146, 0.2351],      
    [0.53155, 0.23693, 0.231],      
    [0.52754, 0.23239, 0.22688],      
    [0.52349, 0.22787, 0.22273],      
    [0.5194, 0.22336, 0.21855],      
    [0.51526, 0.21885, 0.21434],      
    [0.51109, 0.21436, 0.2101],      
    [0.50688, 0.20987, 0.20587],      
    [0.50265, 0.2054, 0.20158],      
    [0.4984, 0.20092, 0.19733],      
    [0.49411, 0.19651, 0.19304],      
    [0.48979, 0.19205, 0.18876],      
    [0.48546, 0.18765, 0.18446],      
    [0.4811, 0.18319, 0.18015],      
    [0.47673, 0.1788, 0.17585],      
    [0.47234, 0.1744, 0.17157],      
    [0.46793, 0.17, 0.1673],      
    [0.4635, 0.16557, 0.16302],      
    [0.45906, 0.16122, 0.15875],      
    [0.4546, 0.15682, 0.15447],      
    [0.45012, 0.15241, 0.15024],      
    [0.44561, 0.14803, 0.14601],      
    [0.4411, 0.14364, 0.14178],      
    [0.43658, 0.13921, 0.1376],      
    [0.43203, 0.13486, 0.1334],      
    [0.42746, 0.13045, 0.12923],      
    [0.42286, 0.12601, 0.1251],      
    [0.41826, 0.12152, 0.12097],      
    [0.41364, 0.11708, 0.11692],      
    [0.409, 0.11265, 0.11291],      
    [0.40433, 0.1081, 0.10886],      
    [0.39965, 0.10363, 0.10484],      
    [0.39496, 0.099059, 0.10092],      
    [0.39024, 0.094525, 0.096994],      
    [0.3855, 0.089888, 0.093119],      
    [0.38077, 0.085202, 0.089344],      
    [0.376, 0.080518, 0.085505],      
    [0.3712, 0.075751, 0.081859],      
    [0.36642, 0.070994, 0.078058],      
    [0.36162, 0.066081, 0.074313],      
    [0.35684, 0.061064, 0.070322],      
    [0.35204, 0.056052, 0.066182],      
    [0.34729, 0.050813, 0.061797],      
    [0.34252, 0.045462, 0.057219],      
    [0.33776, 0.039997, 0.052327],      
    [0.33304, 0.034289, 0.047198],      
    [0.32831, 0.028994, 0.041679],      
    [0.3236, 0.023947, 0.03572],      
    [0.31891, 0.01913, 0.029528],      
    [0.31424, 0.014539, 0.023554],      
    [0.30961, 0.0099596, 0.017575],      
    [0.30498, 0.0058132, 0.011559],      
    [0.30038, 0.0018649, 0.005395]]            
# bilbao_cmap = LinearSegmentedColormap.from_list('bilbao', bilbao_cmdata)
mappy_rgb = numpy.array(bilbao_cmdata)
mappy_name = 'scientific colormaps 7 - bilbao'
fig = colormappy_figure(mappy_rgb, color_name=mappy_name)
fig = colormappy_attributes(mappy_rgb, color_name=mappy_name)
fig = scatter3D_Jpapbp(mappy_rgb, color_name=mappy_name)
fig = surface_sombrero(mappy_rgb, color_name=mappy_name)

plt.show()