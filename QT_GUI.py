import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore

import qdarkstyle
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
- 

"""

class MFParser(QWidget):
    filename = ""
    contents = ""
    bedLevelFilter = ["Raw bed readings"]

    def __init__(self):
        super().__init__()
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
        searching.stip_bed_values(MFParser.logfile(self,MFParser.bedLevelFilter))

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

    def initUI(self):
        filter = []

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

        def quickinfobutt(filename):
            print("quick info")
            tempa = ["\"printTime\":"]

            a = MFParser.logfile(self,tempa)
            abc = searching.printtime(a)
            quickinfotime.setText("Quick Info: "+abc)

        def ParsingWindow():
            try:
                content = self.logfile(filter)
                string = ""
                for i in range(len(content)):
                    string = string + content[i]
                parseddata.setText(string)
            except:
                parseddata.setText("Choose a better file, NERD\nEiger.io -> Printers -> Download Log")

        app.setStyle("Fusion")
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        app.setApplicationName("Markforged Log parser")
        QSize()


        toplabel = QLabel("Markforged Log Parser")
        author = QLabel("Author: Jason Giroux - Python 3.7 Using QT5")

        parsebutton = QPushButton("Parse Log")
        browsebutton = QPushButton("Browse")#browse button
        bedlevelbutton = QPushButton("Bed Leveling Data")
        quickinfoButton = QPushButton("Calculate Quick Info")

        # quickinfolabel = QLabel("Quick Info:")
        printtimelabel = QLabel("print Time:")
        quickinfotime = QLabel()

        bedlevelingfilter = QCheckBox("Bed Leveling Data")
        warnings = QCheckBox("WARNINGS")
        BED = QCheckBox("BED")
        ERRORS = QCheckBox("ERRORS")
        FAILS = QCheckBox("FAILS")
        LEVELOUTPUT = QCheckBox("LEVEL OUTPUT")
        PRINTTIME = QCheckBox("PRINT TIME")
        PRINTJOB = QCheckBox("PRINT JOB INITIALIZATION")


        parseddata = QTextEdit()
        # parseddata.setGeometry(600,600)
        parseddataContainer = QHBoxLayout()
        parseddataContainer.addWidget(parseddata)

        #button pressed events
        browsebutton.clicked.connect(self.Broweserbutton)
        bedlevelbutton.clicked.connect(lambda:MFParser.bedlevel(self))
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

        # define vbox for filters
        filtervboxleft = QHBoxLayout()
        filtervboxleft.addWidget(bedlevelingfilter)
        filtervboxleft.addWidget(warnings)
        filtervboxleft.addWidget(BED)
        filtervboxleft.addWidget(ERRORS)

        filtervboxright = QHBoxLayout()
        filtervboxright.addWidget(FAILS)
        filtervboxright.addWidget(LEVELOUTPUT)
        filtervboxright.addWidget(PRINTTIME)
        filtervboxright.addWidget(PRINTJOB)

        filterhbox = QHBoxLayout()
        filterhbox.addLayout(filtervboxleft)
        filterhbox.addLayout(filtervboxright)

        """
        will need to add filters here
        """
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
        finalVBOX.addLayout(parseddataContainer)

        self.setLayout(finalVBOX)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = MFParser()
    sys.exit(app.exec_())