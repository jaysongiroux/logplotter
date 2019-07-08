import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import numpy as np


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm

import matplotlib.pyplot as plt

import random

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0,0)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500,0)
        button.resize(140,100)

        self.show()


class PlotCanvas(FigureCanvas):
    def xcords(self,mesh):
        tempx = [i[0] for i in mesh]
        tempx = np.asarray(tempx)
        return tempx

    def ycords(self,mesh):
        tempy = [i[1] for i in mesh]
        tempy = np.asarray(tempy)
        return tempy

    def zcords(self,mesh):
        tempz = [i[2] for i in mesh]
        tempz = np.asarray(tempz)
        return tempz

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)


        # self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        mesh = [[11.0, 60.0, -0.066], [33.0, 60.0, -0.0532], [55.0, 60.0, -0.0444], [77.0, 60.0, -0.0276], [99.0, 60.0, -0.0198], [121.0, 60.0, -0.007], [143.0, 60.0, -0.0016], [165.0, 60.0, -0.0007], [187.0, 60.0, 0.0054], [209.0, 60.0, 0.0012], [231.0, 60.0, 0.0044], [253.0, 60.0, -0.0037], [275.0, 60.0, -0.0179], [297.0, 60.0, -0.0437], [319.0, 60.0, -0.067], [319.0, 95.0, -0.0463], [297.0, 95.0, -0.0199], [275.0, 95.0, 0.0079], [253.0, 95.0, 0.0264], [231.0, 95.0, 0.0349], [209.0, 95.0, 0.0333], [187.0, 95.0, 0.0353], [165.0, 95.0, 0.0321], [143.0, 95.0, 0.0314], [121.0, 95.0, 0.0254], [99.0, 95.0, 0.0149], [77.0, 95.0, 0.0033], [55.0, 95.0, -0.0135], [33.0, 95.0, -0.0266], [11.0, 95.0, -0.0395], [11.0, 130.0, -0.046], [33.0, 130.0, -0.0364], [55.0, 130.0, -0.021], [77.0, 130.0, -0.0046], [99.0, 130.0, 0.0103], [121.0, 130.0, 0.022], [143.0, 130.0, 0.029], [165.0, 130.0, 0.0269], [187.0, 130.0, 0.0302], [209.0, 130.0, 0.026], [231.0, 130.0, 0.0254], [253.0, 130.0, 0.0156], [275.0, 130.0, -0.004], [297.0, 130.0, -0.0328], [319.0, 130.0, -0.061], [319.0, 165.0, -0.0727], [297.0, 165.0, -0.0458], [275.0, 165.0, -0.0145], [253.0, 165.0, 0.0072], [231.0, 165.0, 0.0195], [209.0, 165.0, 0.0205], [187.0, 165.0, 0.0262], [165.0, 165.0, 0.023], [143.0, 165.0, 0.025], [121.0, 165.0, 0.0198], [99.0, 165.0, 0.0074], [77.0, 165.0, -0.0089], [55.0, 165.0, -0.0258], [33.0, 165.0, -0.0396], [11.0, 165.0, -0.0504], [11.0, 200.0, -0.0481], [33.0, 200.0, -0.0376], [55.0, 200.0, -0.0277], [77.0, 200.0, -0.0118], [99.0, 200.0, 0.003], [121.0, 200.0, 0.0145], [143.0, 200.0, 0.0197], [165.0, 200.0, 0.0159], [187.0, 200.0, 0.0171], [209.0, 200.0, 0.012], [231.0, 200.0, 0.0109], [253.0, 200.0, -0.0022], [275.0, 200.0, -0.0198], [297.0, 200.0, -0.0522], [319.0, 200.0, -0.0761], [319.0, 235.0, -0.0697], [297.0, 235.0, -0.0451], [275.0, 235.0, -0.016], [253.0, 235.0, 0.003], [231.0, 235.0, 0.0146], [209.0, 235.0, 0.0107], [187.0, 235.0, 0.0174], [165.0, 235.0, 0.0173], [143.0, 235.0, 0.0235], [121.0, 235.0, 0.02], [99.0, 235.0, 0.0116], [77.0, 235.0, -0.0017], [55.0, 235.0, -0.0167], [33.0, 235.0, -0.0276], [11.0, 235.0, -0.0378], [11.0, 270.0, -0.0213], [33.0, 270.0, -0.0153], [55.0, 270.0, -0.0087], [77.0, 270.0, 0.0068], [99.0, 270.0, 0.0163], [121.0, 270.0, 0.0246], [143.0, 270.0, 0.0279], [165.0, 270.0, 0.0216], [187.0, 270.0, 0.0228], [209.0, 270.0, 0.0153], [231.0, 270.0, 0.0184], [253.0, 270.0, 0.0071], [275.0, 270.0, -0.0103], [297.0, 270.0, -0.0409], [319.0, 270.0, -0.0616]]
        x = self.xcords(mesh)
        y = self.ycords(mesh)
        z = self.zcords(mesh)

        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)

        ax = self.figure.gca(projection='3d')
        ax.plot_surface(x,y,z,rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=True)
        # ax.plot_surface(x, y, z)
        # ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
