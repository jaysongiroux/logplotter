import sys
from PyQt5.QtWidgets import *
import qdarkstyle
import searching
import graph_qt_GUI

# stip_bed_values(logfile(filename,True,bedLevelFilter))

class MFParser(QWidget):
    filename = ""
    contents = ""
    bedLevelFilter= ["Raw bed readings"]

    def __init__(self):
        super().__init__()
        self.initUI()

    #returns the filename the user selected
    def Broweserbutton(self):
        print("browse was clicked")
        global filename
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        filename = fname[0]
        print(filename)

    def bedlevel(self):
        print("bed leveling was pressed")
        searching.stip_bed_values(MFParser.logfile(self,MFParser.bedLevelFilter))
        # graph_qt_GUI.App(MFParser.logfile(self,MFParser.bedLevelFilter))

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

    def parsedGUI(self):
        app = QApplication([])




    def initUI(self):
        filter = []

        def alterfilter(a,b,bool=False): #bool means the filter needs to add more than one value to the array
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

            a = MFParser.logfile( self ,tempa)
            abc = searching.printtime(a)
            quickinfotime.setText(abc)


        app.setStyle("Fusion")
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        app.setApplicationName("Markforged Log parser")

        toplabel = QLabel("Markforged Log Parser")
        author = QLabel("Author: Jason Giroux - Python 3.7 Using QT5")

        featurelabel = QLabel("Features")
        filterslabel = QLabel("Filters")
        parsebutton = QPushButton("Parse Log")
        browsebutton = QPushButton("Browse")#browse button
        bedlevelbutton = QPushButton("Bed Leveling Data")
        quickinfoButton = QPushButton("Calculate Quick Info")

        quickinfolabel = QLabel("Quick Info:")
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


        #button pressed events
        browsebutton.clicked.connect(self.Broweserbutton)
        bedlevelbutton.clicked.connect(lambda:MFParser.bedlevel(self))
        parsebutton.clicked.connect(lambda:MFParser.logfile(self,filter))
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

        titleshbox = QHBoxLayout()
        titleshbox.addWidget(filterslabel)
        titleshbox.addWidget(featurelabel)

        # define vbox for filters
        filtervboxleft = QVBoxLayout()
        filtervboxleft.addWidget(bedlevelingfilter)
        filtervboxleft.addWidget(warnings)
        filtervboxleft.addWidget(BED)
        filtervboxleft.addWidget(ERRORS)

        filtervboxright = QVBoxLayout()
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
        buttonHbox = QVBoxLayout()
        buttonHbox.addWidget(browsebutton)
        buttonHbox.addWidget(parsebutton)
        buttonHbox.addWidget(bedlevelbutton)
        buttonHbox.addWidget(quickinfoButton)

        #define quick info hbox
        quickinfohbox = QHBoxLayout()
        quickinfohbox.addWidget(quickinfolabel)
        quickinfohbox.addWidget(quickinfotime)

        #define quick info info vbox
        quickinfoinfo = QVBoxLayout()
        quickinfoinfo.addWidget(printtimelabel)

        middlehbox = QHBoxLayout()
        middlehbox.addLayout(filterhbox)
        middlehbox.addLayout(buttonHbox)  #filtervbox

        #defining the final VBOX
        finalVBOX = QVBoxLayout()
        finalVBOX.addLayout(welcomehbox) #,middlehbox,quickinfohbox
        finalVBOX.addLayout(titleshbox)
        finalVBOX.addLayout(middlehbox)
        finalVBOX.addLayout(quickinfohbox)

        self.setLayout(finalVBOX)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = MFParser()
    sys.exit(app.exec_())