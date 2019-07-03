import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal

"""
average offset from zero using the average as 0

todo:
make z min and max scale depending on min and max of the array
make third graph with offset array
"""

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

"""
todo:
1. 2D top down view similar to how prusa does it.
"""

def graphtoolpath(mesh):
    fig = plt.figure(figsize = (13, 8))
    ax = fig.add_subplot(221, projection='3d')

    x = xcords(mesh)
    y = ycords(mesh)
    z = zcords(mesh)

    ax.plot3D(x,y,z,'gray')
    ax.plot_trisurf(x,y,z,cmap='Reds') #surface
    ax.set_zlim(-.5, .5)

    plt.title('Bed leveling')
    plt.xlabel('X Axis (mm)')
    ax.set_ylabel('Y Axis (mm)')
    ax.set_zlabel('Z Axis (um)')

    toolpath = fig.add_subplot(222, projection='3d')

    toolpath.plot3D(x, y, z, 'gray')

    toolpath.scatter3D(x, y, z, c=z, cmap='Greys')
    toolpath.set_zlim(-.5, .5)

    plt.title('Tool Path')
    toolpath.set_xlabel('X Axis (mm)')
    toolpath.set_ylabel('Y Axis (mm)')
    toolpath.set_zlabel('Z Axis (um)')


    #temp for now, will add seperate GUI
    labels = fig.add_subplot(223)
    info = fig.add_subplot(224)
    txt = "Max: {} \u03BCm\n Min: {} \u03BCm\n Average: {} \u03BCm\n Deviation: {}  \u03BCm\n Average Offset: {} \u03BCm ".format(round(maxi(mesh),4),round(mini(mesh),4),round(average1(z),4),round(dev(maxi(mesh),mini(mesh)),4),'%.2E' % Decimal(offset(z)),4)

    labels.text(0.5, 0.5, txt, size=24, ha='center', va='center') #max
    labels.axis('off')
    info.axis('off')


    plt.setp(labels.get_xticklabels(), visible=False)
    plt.setp(labels.get_yticklabels(), visible=False)

    plt.show()



