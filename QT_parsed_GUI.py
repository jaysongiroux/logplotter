import PyQt5
import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore
import qdarkstyle
from PyQt5.QtCore import QSize

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

"""
average offset from zero using the average as 0

todo:
make z min and max scale depending on min and max of the array
make third graph with offset array
- make infomation container and display everything
"""

class Parsing(QDialog):
    def __init__(self, parent=None,content=""):#mesh is being passed corectly
        self.content = content
        app = QApplication(sys.argv)
        super(Parsing, self).__init__(parent)

        #styling
        app.setStyle("Fusion")
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

        #defining the figure the gui is placed on
        self.figure = Figure()
        app.setApplicationName("Markforged Log parser")

        self.lowerHBox = QHBoxLayout()

        self.toplabel = QLabel("Markforged Log Parser")
        self.author = QLabel("Author: Jason Giroux - Python 3.7 Using QT5")

        self.lowerHBox.addWidget(self.toplabel)
        self.lowerHBox.addWidget(self.author)

        self.middleHBox = QHBoxLayout()

        self.canvas = FigureCanvas(self.figure) #this is where the graph is in the QT GUI

        self.lowerVBoxRight = QVBoxLayout()
        self.lowerVBoxLeft = QVBoxLayout()

        #adding containers for grid-like layout
        self.lowerHBox.addLayout(self.middleHBox)

        # set the layout & toolbar
        layout = QVBoxLayout()

        layout.addWidget(self.canvas)
        layout.addLayout(self.lowerHBox)

        self.canvas.draw()
        self.setLayout(layout)
        self.show()


    def sizeHint(self):
        return QSize(800,500)

    def sizeForWidth(self,width):
        return width*.5

