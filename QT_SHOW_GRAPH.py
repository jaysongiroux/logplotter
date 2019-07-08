import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette
import PyQt5.QtCore as Qt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
import qdarkstyle
from PyQt5.QtCore import QSize


"""
average offset from zero using the average as 0

todo:
make z min and max scale depending on min and max of the array
make third graph with offset array
- make infomation container and display everything
"""

def xcords(mesh):
    tempx = [i[0] for i in mesh]
    return tempx

def ycords(mesh):
    tempy = [i[1] for i in mesh]
    return tempy

def zcords(mesh):
    tempz = [i[2] for i in mesh]
    return tempz

def offset(mesh):
    offset = np.zeros(len(mesh))
    zero = average1(mesh)
    for i in range(len(mesh)):
        offset[i] = zero - mesh[i]
    average = np.average(offset)
    return average * 1000 #returns in MM

def average1(mesh):
    tempz = mesh
    length = len(tempz)
    adding = np.sum(tempz)
    ave = adding / length
    return round(ave, 10)


class Window(QDialog):
    def __init__(self, parent=None,mesh=""):#mesh is being passed corectly
        self.mesh = mesh
        app = QApplication(sys.argv)
        super(Window, self).__init__(parent)

        def zcords(mesh):
            tempz = [i[2] for i in mesh]
            return tempz

        def offset(mesh):
            offset =[]
            zero = average1(mesh)
            for i in range(len(mesh)):
                offset.append(zero - mesh[i])
            average = np.average(offset)
            print("Offset Average:",average)
            return average


        #styling
        app.setStyle("Fusion")
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

        #defining the figure the gui is placed on
        self.figure = Figure()

        #defining the canvas on the figure
        self.canvas = FigureCanvas(self.figure) #this is where the graph is in the QT GUI
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.lowerHBox = QHBoxLayout()
        self.lowerVBoxRight = QVBoxLayout()
        self.lowerVBoxLeft = QVBoxLayout()


        #calculating information on given mesh
        #fix offset
        self.offset = QLabel("Average Offset: "+str(round(offset(zcords(mesh)),12))+" mm")
        self.average = QLabel("Average"+str(average1(zcords(mesh)))+" um")
        self.maximum = QLabel("Maximum"+str(np.max(zcords(mesh)))+" um")
        self.minimum = QLabel("Minimum"+str(np.min(zcords(mesh)))+" um")

        self.dev = np.max(zcords(mesh)) - np.min(zcords(mesh))
        self.dev = QLabel("Average Deviation: "+str(self.dev)+" um")


        self.lowerVBoxLeft.addWidget(self.offset)
        self.lowerVBoxLeft.addWidget(self.average)
        self.lowerVBoxLeft.addWidget(self.maximum)
        self.lowerVBoxLeft.addWidget(self.minimum)
        self.lowerVBoxLeft.addWidget(self.dev)


        #adding containers for grid-like layout
        self.lowerHBox.addLayout(self.lowerVBoxLeft)
        self.lowerHBox.addLayout(self.lowerVBoxRight)
        self.graphtoolpath()

        # set the layout & toolbar
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addLayout(self.lowerHBox)

        #definign the lax VBOX everything is placed in
        self.setLayout(layout)
        self.show()

    def graphtoolpath(self):  # mesh is a 2d array with XYZ cords
        x = xcords(self.mesh)
        y = ycords(self.mesh)
        z = zcords(self.mesh)
        ax = self.figure.add_subplot(121, projection='3d')
        # ax = self.figure.gca(projection='3d')
        ax.plot_trisurf(x, y, z, cmap=cm.coolwarm)
        ax.set_zlim(-.3, .3)

        ax.set_xlabel('X Axis (mm)')
        ax.set_ylabel('Y Axis (mm)')
        ax.set_zlabel('Z Axis (um)')
        #-----------Graph 2:
        toolpath = self.figure.add_subplot(122,projection='3d')
        toolpath.plot3D(x,y,z, 'grey')
        toolpath.scatter3D(x, y, z, c=z, cmap='Greys')
        toolpath.set_zlim(-.3, .3)
        toolpath.set_xlabel('X Axis (mm)')
        toolpath.set_ylabel('Y Axis (mm)')
        toolpath.set_zlabel('Z Axis (um)')


        self.canvas.draw()

    def sizeHint(self):
        return QSize(800,500)

    def sizeForWidth(self,width):
        return width*.5

