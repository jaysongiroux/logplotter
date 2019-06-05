import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec


log_mesh = np.array([[11.0, 60.0, 0.1604], [33.0, 60.0, 0.1591], [55.0, 60.0, 0.1538], [77.0, 60.0, 0.1708], [99.0, 60.0, 0.1818], [121.0, 60.0, 0.1846], [143.0, 60.0, 0.1923], [165.0, 60.0, 0.1913], [187.0, 60.0, 0.1941], [209.0, 60.0, 0.2007], [231.0, 60.0, 0.21], [253.0, 60.0, 0.2183], [275.0, 60.0, 0.2109], [297.0, 60.0, 0.2041], [319.0, 60.0, 0.2095], [319.0, 95.0, 0.2069], [297.0, 95.0, 0.2086], [275.0, 95.0, 0.2192], [253.0, 95.0, 0.2321], [231.0, 95.0, 0.2293], [209.0, 95.0, 0.2208], [187.0, 95.0, 0.2176], [165.0, 95.0, 0.2137], [143.0, 95.0, 0.2146], [121.0, 95.0, 0.2053], [99.0, 95.0, 0.1996], [77.0, 95.0, 0.1906], [55.0, 95.0, 0.1743], [33.0, 95.0, 0.17], [11.0, 95.0, 0.1726], [11.0, 130.0, 0.1891], [33.0, 130.0, 0.1863], [55.0, 130.0, 0.1898], [77.0, 130.0, 0.2005], [99.0, 130.0, 0.2081], [121.0, 130.0, 0.2151], [143.0, 130.0, 0.2224], [165.0, 130.0, 0.2151], [187.0, 130.0, 0.2161], [209.0, 130.0, 0.215], [231.0, 130.0, 0.2246], [253.0, 130.0, 0.2288], [275.0, 130.0, 0.2221], [297.0, 130.0, 0.2096], [319.0, 130.0, 0.2024], [319.0, 165.0, 0.1972], [297.0, 165.0, 0.2102], [275.0, 165.0, 0.2239], [253.0, 165.0, 0.2381], [231.0, 165.0, 0.2335], [209.0, 165.0, 0.2293], [187.0, 165.0, 0.2328], [165.0, 165.0, 0.2324], [143.0, 165.0, 0.2387], [121.0, 165.0, 0.2334], [99.0, 165.0, 0.227], [77.0, 165.0, 0.2201], [55.0, 165.0, 0.2101], [33.0, 165.0, 0.2044], [11.0, 165.0, 0.2012], [11.0, 200.0, 0.2008], [33.0, 200.0, 0.1952], [55.0, 200.0, 0.1894], [77.0, 200.0, 0.1912], [99.0, 200.0, 0.1958], [121.0, 200.0, 0.2009], [143.0, 200.0, 0.2027], [165.0, 200.0, 0.1937], [187.0, 200.0, 0.1945], [209.0, 200.0, 0.1886], [231.0, 200.0, 0.1989], [253.0, 200.0, 0.2], [275.0, 200.0, 0.1868], [297.0, 200.0, 0.1742], [319.0, 200.0, 0.1624], [319.0, 235.0, 0.1535], [297.0, 235.0, 0.1644], [275.0, 235.0, 0.1739], [253.0, 235.0, 0.1923], [231.0, 235.0, 0.2007], [209.0, 235.0, 0.1972], [187.0, 235.0, 0.2032], [165.0, 235.0, 0.2], [143.0, 235.0, 0.2127], [121.0, 235.0, 0.2092], [99.0, 235.0, 0.2084], [77.0, 235.0, 0.2053], [55.0, 235.0, 0.2019], [33.0, 235.0, 0.2036], [11.0, 235.0, 0.2095], [11.0, 270.0, 0.2439], [33.0, 270.0, 0.2284], [55.0, 270.0, 0.2231], [77.0, 270.0, 0.2229], [99.0, 270.0, 0.2214], [121.0, 270.0, 0.2222], [143.0, 270.0, 0.221], [165.0, 270.0, 0.2033], [187.0, 270.0, 0.2019], [209.0, 270.0, 0.1888], [231.0, 270.0, 0.1874], [253.0, 270.0, 0.1818], [275.0, 270.0, 0.1744], [297.0, 270.0, 0.1661], [319.0, 270.0, 0.1504]])

def xcords(mesh):
    tempx = [i[0] for i in mesh]
    # x = np.arange(tempx)
    return tempx

def ycords(mesh):
    tempy = [i[1] for i in mesh]
    # y = np.arange(tempy)
    return tempy

def zcords(mesh):
    tempz = [i[2] for i in mesh]
    # for i in range(len(tempz)):
        # tempz[i]=tempz[i]/1000
    # z = np.arange(tempz)
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
    tempz = zcords(mesh)
    length = len(tempz)
    adding = np.sum(tempz)
    ave = adding/length
    print(ave)
    return round(ave,4)

def graphtoolpath(mesh):
    fig = plt.figure(figsize = (13, 8))
    ax = fig.add_subplot(221, projection='3d')
    # x = y = np.arange(0, 300, 50) #min, max, steps
    x = xcords(mesh)
    y = ycords(mesh)
    z = zcords(mesh)

    # print(x)
    # print("---")
    # print(y)
    X,Y,Z= np.meshgrid(x, y,z)
    ax.plot3D(x,y,z,'gray')
    ax.plot_trisurf(x,y,z,cmap='Reds') #surface
    ax.set_zlim(0, .5)

    #ax.plot3D(x,y,z,'gray') #tool path
    # ax.scatter3D(x,y,z,c=z,cmap='Greys')
    #now to work on z cords
    # print("shape",X.shape)
    #
    # Z = zs.reshape(X.shape)
    # print(np.array(Z))
    # ax.plot_surface(X, Y, Z)
    plt.title('Bed Leveling')
    plt.xlabel('X Axis (mm)')
    ax.set_ylabel('Y Axis (mm)')
    ax.set_zlabel('Z Axis (um)')


    toolpath = fig.add_subplot(222, projection='3d')
    x = xcords(mesh)
    y = ycords(mesh)
    z = zcords(mesh)
    # print(x)
    # print("---")
    # print(y)
    X, Y, Z = np.meshgrid(x, y, z)
    toolpath.plot3D(x, y, z, 'gray')
    # toolpath.plot_trisurf(x, y, z, cmap='Reds')  # surface
    # ax.plot3D(x,y,z,'gray') #tool path
    toolpath.scatter3D(x, y, z, c=z, cmap='Greys')
    toolpath.set_zlim(0, .5)

    # now to work on z cords
    # print("shape",X.shape)
    #
    # Z = zs.reshape(X.shape)
    # print(np.array(Z))
    # ax.plot_surface(X, Y, Z)
    plt.title('Tool Path')
    toolpath.set_xlabel('X Axis (mm)')
    toolpath.set_ylabel('Y Axis (mm)')
    toolpath.set_zlabel('Z Axis (um)')


    #temp for now, will add seperate GUI
    labels = fig.add_subplot(223)
    info = fig.add_subplot(224)
    labels.text(0.5, 0.5, "Max: {} \n Min: {} \n Average: {}".format(maxi(mesh),mini(mesh),average1(mesh)), size=24, ha='center', va='center') #max


    plt.setp(labels.get_xticklabels(), visible=False)
    plt.setp(labels.get_yticklabels(), visible=False)

    plt.show()


graphtoolpath(log_mesh)