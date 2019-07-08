import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

"""
average offset from zero using the average as 0

todo:
make z min and max scale depending on min and max of the array
make third graph with offset array
"""
mesh = [[11.0, 60.0, -0.066], [33.0, 60.0, -0.0532], [55.0, 60.0, -0.0444], [77.0, 60.0, -0.0276],
        [99.0, 60.0, -0.0198], [121.0, 60.0, -0.007], [143.0, 60.0, -0.0016], [165.0, 60.0, -0.0007],
        [187.0, 60.0, 0.0054], [209.0, 60.0, 0.0012], [231.0, 60.0, 0.0044], [253.0, 60.0, -0.0037],
        [275.0, 60.0, -0.0179], [297.0, 60.0, -0.0437], [319.0, 60.0, -0.067], [319.0, 95.0, -0.0463],
        [297.0, 95.0, -0.0199], [275.0, 95.0, 0.0079], [253.0, 95.0, 0.0264], [231.0, 95.0, 0.0349],
        [209.0, 95.0, 0.0333], [187.0, 95.0, 0.0353], [165.0, 95.0, 0.0321], [143.0, 95.0, 0.0314],
        [121.0, 95.0, 0.0254], [99.0, 95.0, 0.0149], [77.0, 95.0, 0.0033], [55.0, 95.0, -0.0135], [33.0, 95.0, -0.0266],
        [11.0, 95.0, -0.0395], [11.0, 130.0, -0.046], [33.0, 130.0, -0.0364], [55.0, 130.0, -0.021],
        [77.0, 130.0, -0.0046], [99.0, 130.0, 0.0103], [121.0, 130.0, 0.022], [143.0, 130.0, 0.029],
        [165.0, 130.0, 0.0269], [187.0, 130.0, 0.0302], [209.0, 130.0, 0.026], [231.0, 130.0, 0.0254],
        [253.0, 130.0, 0.0156], [275.0, 130.0, -0.004], [297.0, 130.0, -0.0328], [319.0, 130.0, -0.061],
        [319.0, 165.0, -0.0727], [297.0, 165.0, -0.0458], [275.0, 165.0, -0.0145], [253.0, 165.0, 0.0072],
        [231.0, 165.0, 0.0195], [209.0, 165.0, 0.0205], [187.0, 165.0, 0.0262], [165.0, 165.0, 0.023],
        [143.0, 165.0, 0.025], [121.0, 165.0, 0.0198], [99.0, 165.0, 0.0074], [77.0, 165.0, -0.0089],
        [55.0, 165.0, -0.0258], [33.0, 165.0, -0.0396], [11.0, 165.0, -0.0504], [11.0, 200.0, -0.0481],
        [33.0, 200.0, -0.0376], [55.0, 200.0, -0.0277], [77.0, 200.0, -0.0118], [99.0, 200.0, 0.003],
        [121.0, 200.0, 0.0145], [143.0, 200.0, 0.0197], [165.0, 200.0, 0.0159], [187.0, 200.0, 0.0171],
        [209.0, 200.0, 0.012], [231.0, 200.0, 0.0109], [253.0, 200.0, -0.0022], [275.0, 200.0, -0.0198],
        [297.0, 200.0, -0.0522], [319.0, 200.0, -0.0761], [319.0, 235.0, -0.0697], [297.0, 235.0, -0.0451],
        [275.0, 235.0, -0.016], [253.0, 235.0, 0.003], [231.0, 235.0, 0.0146], [209.0, 235.0, 0.0107],
        [187.0, 235.0, 0.0174], [165.0, 235.0, 0.0173], [143.0, 235.0, 0.0235], [121.0, 235.0, 0.02],
        [99.0, 235.0, 0.0116], [77.0, 235.0, -0.0017], [55.0, 235.0, -0.0167], [33.0, 235.0, -0.0276],
        [11.0, 235.0, -0.0378], [11.0, 270.0, -0.0213], [33.0, 270.0, -0.0153], [55.0, 270.0, -0.0087],
        [77.0, 270.0, 0.0068], [99.0, 270.0, 0.0163], [121.0, 270.0, 0.0246], [143.0, 270.0, 0.0279],
        [165.0, 270.0, 0.0216], [187.0, 270.0, 0.0228], [209.0, 270.0, 0.0153], [231.0, 270.0, 0.0184],
        [253.0, 270.0, 0.0071], [275.0, 270.0, -0.0103], [297.0, 270.0, -0.0409], [319.0, 270.0, -0.0616]]


def offset(mesh):
    offset = np.zeros(len(mesh))
    zero = average1(mesh)
    for i in range(len(mesh)):
        offset[i] = zero - mesh[i]
    average = np.average(offset)
    return average

def xcords(mesh):
    tempx = [i[0] for i in mesh]
    return tempx

def ycords(mesh):
    tempy = [i[1] for i in mesh]
    return tempy

def zcords(mesh):
    tempz = [i[2] for i in mesh]
    return tempz

def maxi(mesh):
    tempz = zcords(mesh)
    max = np.max(tempz)
    return max

def mini(mesh):
    tempz = zcords(mesh)
    min = np.min(tempz)
    return min

def average1(mesh):
    tempz = mesh
    length = len(tempz)
    adding = np.sum(tempz)
    ave = adding/length
    return round(ave,10)

def dev(max,min):
    return max - min


def graphtoolpath(mesh): #mesh is a 2d array with XYZ cords
    x = xcords(mesh)
    y = ycords(mesh)
    z = zcords(mesh)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_trisurf(x,y,z,cmap=cm.coolwarm)
    plt.show()
    #
    # print("graphing tool path")
    #
    # fig = plt.figure(figsize = (13, 8)) #
    #
    # ax = fig.add_subplot(221, projection='3d')



    # print("graphing tool path")
    # ax.plot3D(x,y,z,'gray')
    # ax.plot_trisurf(x,y,z,cmap='Reds') #surface
    # ax.set_zlim(-.5, .5)

    # plt.title('Bed leveling')
    # plt.xlabel('X Axis (mm)')
    #
    # ax.set_ylabel('Y Axis (mm)')
    # ax.set_zlabel('Z Axis (um)')
    # print("graphing tool path")

    #
    # toolpath = fig.add_subplot(222, projection='3d')
    #
    # toolpath.plot3D(x, y, z, 'gray')
    #
    # toolpath.scatter3D(x, y, z, c=z, cmap='Greys')
    # toolpath.set_zlim(-.5, .5)
    #
    # plt.title('Tool Path')
    # toolpath.set_xlabel('X Axis (mm)')
    # toolpath.set_ylabel('Y Axis (mm)')
    # toolpath.set_zlabel('Z Axis (um)')


    #temp for now, will add seperate GUI
    # labels = fig.add_subplot(223)
    # info = fig.add_subplot(224)
    # txt = "Max: {} \u03BCm\n Min: {} \u03BCm\n Average: {} \u03BCm\n Deviation: {}  \u03BCm\n Average Offset: {} \u03BCm ".format(round(maxi(mesh),4),round(mini(mesh),4),round(average1(z),4),round(dev(maxi(mesh),mini(mesh)),4),'%.2E' % Decimal(offset(z)),4)

    # labels.text(0.5, 0.5, txt, size=24, ha='center', va='center') #max
    # labels.axis('off')
    # info.axis('off')

    #
    # plt.setp(labels.get_xticklabels(), visible=False)
    # plt.setp(labels.get_yticklabels(), visible=False)

    # plt.show()



