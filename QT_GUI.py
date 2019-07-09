import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import searching
import graph_qt_GUI
import QT_SHOW_GRAPH
from PyQt5.QtWidgets import QApplication
from matplotlib import cm
import numpy as np

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

"""
crashes when you try to open several bed leveling windows at once

todo:
- add a "source code" hyper link in the bottom tool bar
- if i have time, try to get the matlab onto the same GUI so not have to worry about multiple windows

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

class MFParser(QWidget):
    filename = ""
    contents = ""
    bedLevelFilter = ["Raw bed readings"]

    def sizeHint(self):
        return QSize(600, 600)

    def heightForWidth(self, width):
        return width *2

    def __init__(self):
        super().__init__()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
        sizePolicy.setHeightForWidth(True)
        self.initUI()

    # returns the filename the user selected
    def Broweserbutton(self):
        print("browse was clicked")
        global filename
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        filename = fname[0]
        print(filename)

    # change this for different bed leveling information
    def bedlevel(self):
        print("bed leveling was pressed")
        try:
            searching.stip_bed_values(MFParser.logfile(self,MFParser.bedLevelFilter))
        except: pass

    def logfile(self,filter):  # bool is if filters exsist, o is the filter array
        print("reading file")
        global contents
        try:
            if len(filter) > 0:  # if given  filter
                with open(filename, 'r') as u:
                    temp = []
                    numOfFilters = len(filter)
                    for line in u:
                        for i in range(numOfFilters):
                            if filter[i].lower() in line.lower():
                                temp.append(line)
                            else:
                                continue
                    # without applying any filters, a log file is dumped into X
                u.close()  # new to manage memory
                #for row in temp: print (row)
                # print(temp)
                return temp
            # this is when there is no filters
            else:
                with open(filename, 'r') as f:

                    x = f.readlines()
                f.close()  # new to manage memory
                #for row in x: print(row)
                return x
        except:
            print("please choose a file first")

    def graphtoolpath(self,mesh=[]):  # mesh is a 2d array with XYZ cords
        global figure
        x = xcords(mesh)
        y = ycords(mesh)
        z = zcords(mesh)
        ax = self.figure.add_subplot(211, projection='3d')
        # ax = self.figure.gca(projection='3d')
        try:
            ax.plot_trisurf(x, y, z, cmap=cm.coolwarm)
            ax.set_zlim(-.3, .3)
            ax.set_xlabel('X Axis (mm)')
            ax.set_ylabel('Y Axis (mm)')
            ax.set_zlabel('Z Axis (um)')

            #-----------Graph 2:
            toolpath = self.figure.add_subplot(212,projection='3d')
            toolpath.plot3D(x,y,z, 'grey')
            toolpath.scatter3D(x, y, z, c=z, cmap='Greys')
            toolpath.set_zlim(-.3, .3)
            toolpath.set_xlabel('X Axis (mm)')
            toolpath.set_ylabel('Y Axis (mm)')
            toolpath.set_zlabel('Z Axis (um)')

            self.canvas.draw() #draws on the main GUI

        except: pass

    def initUI(self):
        filter = []
        filename =""

        def graphButtonPress():
            mesh = searching.stip_bed_values(MFParser.logfile(self,MFParser.bedLevelFilter))
            MFParser.graphtoolpath(self,mesh=mesh)

        def alterfilter(a,b,bool=False):
            if bool == True:
                 if b ==True:
                     for i in range(len(a)): filter.append(a[i])
                 else:
                    for i in range(len(a)):
                        try: filter.remove(a[i])
                        except: continue
            else:
                if b ==True: filter.append(a)
                else: filter.remove(a)
            print("Filter: ",filter,"Checked: ",b)

        def quickinfobutt(filename=""):
            print("quick info")
            tempa = ["\"printTime\":"]

            a = MFParser.logfile(self,tempa)
            abc = searching.printtime(a)
            quickinfotime.setText("Quick Info: Print Time for Log: "+abc+"\nBed Leveling Data: ")

        def ParsingWindow():
            # try:

            content = self.logfile(filter)
            string = ""
            for i in range(len(content)):
                string = string + content[i]

            self.parseddata.setText(string)
            self.sidebyside.update()
            quickinfobutt(filename)
            graphButtonPress()

            # except:
            # self.parseddata.setText("Choose a better file, NERD\nEiger.io -> Printers -> Download Log")
            # self.parseddata.setLineWrapMode(True)

        app.setStyle("Fusion")
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        app.setApplicationName("Log parser")
        QSize()

        #Top Label
        toplabel = QLabel("Log Parser")
        author = QLabel("Author: Jason Giroux - Python 3.7 Using QT5")
        sourceCode = QLabel("Source Code")

        # tool bar buttons
        parsebutton = QPushButton("Parse Log")
        browsebutton = QPushButton("Browse")#browse button
        bedlevelbutton = QPushButton("Bed Leveling Data")
        quickinfoButton = QPushButton("Calculate Quick Info")

        # quickinfolabel = QLabel("Quick Info:")
        printtimelabel = QLabel("print Time:")
        quickinfotime = QLabel() #will be textset from seperate method
        graphLabel = QLabel("Bed Leveling Data")

        #toolbar check box
        bedlevelingfilter = QCheckBox("Bed Leveling Data")
        warnings = QCheckBox("WARNINGS")
        BED = QCheckBox("BED")
        ERRORS = QCheckBox("ERRORS")
        FAILS = QCheckBox("FAILS")
        LEVELOUTPUT = QCheckBox("LEVEL OUTPUT")
        PRINTTIME = QCheckBox("PRINT TIME")
        PRINTJOB = QCheckBox("PRINT JOB INITIALIZATION")

        #defining graph figures
        def zcords(mesh):
            tempz = [i[2] for i in mesh]
            return tempz

        def average1(mesh):
            tempz = mesh
            length = len(tempz)
            adding = np.sum(tempz)
            ave = adding / length
            return round(ave, 10)

        def offset(mesh):
            offset =[]
            zero = average1(mesh)
            for i in range(len(mesh)):
                offset.append(zero - mesh[i])
            average = np.average(offset)
            print("Offset Average:",average)
            return average

        def xcords(mesh):
            tempx = [i[0] for i in mesh]
            return tempx

        def ycords(mesh):
            tempy = [i[1] for i in mesh]
            return tempy

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure) #this is where the graph is in the QT GUI

        #text edit bottom
        self.parseddata = QTextEdit()
        self.sidebyside = QSplitter()
        self.sidebyside.setOrientation(Qt.Horizontal)

        self.sidebyside.addWidget(self.canvas)
        self.sidebyside.addWidget(self.parseddata)
        self.sidebyside.setBaseSize(10,1)
        self.sidebyside.update()
        # self.sidebyside.addLayout(self.containerGraph)
        # self.sidebyside.addLayout(self.parseddataContainer)

        #button pressed events
        browsebutton.clicked.connect(self.Broweserbutton)
        bedlevelbutton.clicked.connect(lambda:graphButtonPress())#:MFParser.bedlevel(self)
        parsebutton.clicked.connect(lambda:ParsingWindow())  #content=MFParser.logfile(self,filter))
        quickinfoButton.clicked.connect(lambda:quickinfobutt(filename))

        #defining check button functions
        bedlevelingfilter.stateChanged.connect(lambda:alterfilter("RAW",bedlevelingfilter.isChecked()))
        warnings.stateChanged.connect(lambda:alterfilter(["WARNING","WRN"],warnings.isChecked(),True))
        BED.stateChanged.connect(lambda:alterfilter("bed",BED.isChecked()))
        ERRORS.stateChanged.connect(lambda:alterfilter("ERROR",ERRORS.isChecked()))
        FAILS.stateChanged.connect(lambda:alterfilter("fail",FAILS.isChecked()))
        LEVELOUTPUT.stateChanged.connect(lambda:alterfilter("RAW",LEVELOUTPUT.isChecked()))
        PRINTTIME.stateChanged.connect(lambda:alterfilter("\"printTime\":",PRINTTIME.isChecked()))
        PRINTJOB.stateChanged.connect(lambda:alterfilter("Print Job initialization",PRINTJOB.isChecked()))

        #defining the title vbox
        welcomehbox = QVBoxLayout()
        welcomehbox.addWidget(toplabel)
        welcomehbox.addWidget(author)
        welcomehbox.addWidget(sourceCode) #todo: add hyper link

        # define vbox for filters
        filtervboxleft = QHBoxLayout()
        filtervboxleft.addWidget(bedlevelingfilter)
        filtervboxleft.addWidget(warnings)
        filtervboxleft.addWidget(BED)
        filtervboxleft.addWidget(ERRORS)

        #right boxes for filters
        filtervboxright = QHBoxLayout()
        filtervboxright.addWidget(FAILS)
        filtervboxright.addWidget(LEVELOUTPUT)
        filtervboxright.addWidget(PRINTTIME)
        filtervboxright.addWidget(PRINTJOB)

        filterhbox = QHBoxLayout()
        filterhbox.addLayout(filtervboxleft)
        filterhbox.addLayout(filtervboxright)

        buttonHbox = QHBoxLayout()
        buttonHbox.addWidget(browsebutton)
        buttonHbox.addWidget(parsebutton)
        buttonHbox.addWidget(bedlevelbutton)
        buttonHbox.addWidget(quickinfoButton)

        #define quick info hbox
        quickinfohbox = QHBoxLayout()
        # quickinfohbox.addWidget(quickinfolabel)
        quickinfohbox.addWidget(quickinfotime)

        #define quick info info vbox
        quickinfoinfo = QHBoxLayout()
        quickinfoinfo.addWidget(printtimelabel)

        middlehbox = QHBoxLayout()
        middlehbox.addLayout(filterhbox)
        middlehbox.addLayout(buttonHbox)  #filtervbox

        #defining the final VBOX
        finalVBOX = QVBoxLayout()
        finalVBOX.addLayout(welcomehbox) #,middlehbox,quickinfohbox
        finalVBOX.addLayout(middlehbox)
        finalVBOX.addLayout(quickinfohbox)
        finalVBOX.addWidget(self.sidebyside)
        # finalVBOX.addLayout(self.parseddataContainer)

        self.setLayout(finalVBOX)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = MFParser()
    sys.exit(app.exec_())