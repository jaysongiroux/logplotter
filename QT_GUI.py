import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import *




class MFParser(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        app.setStyle("Fusion")

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(palette)
        app.setApplicationName("Markforged Log parser")

        """
        filters:
         cb1 = Checkbutton(r, text='"WARNINGS', variable=w,onvalue="WARNING",offvalue="").grid(row=5, column=0,sticky="w")
        cb2 = Checkbutton(r, text='BED', variable=b,onvalue="bed",offvalue="").grid(row=5, column=1,sticky="w")
        cb3 = Checkbutton(r, text='ERRORS', variable=e, onvalue="ERROR",offvalue="").grid(row=6, column=0,sticky="w")
        cb4 = Checkbutton(r, text='FAILS', variable=f,onvalue="fail",offvalue="").grid(row=6, column=1,sticky="w")
        cb5 = Checkbutton(r, text='LEVEL OUTPUT', variable=l,onvalue="Raw",offvalue="").grid(row=7, column=0,sticky="w")
        cb6 = Checkbutton(r, text='PRINT TIME', variable=q,onvalue="\"printTime\":",offvalue="").grid(row=7,column=1,sticky="w")
        cb7 = Checkbutton(r, text='Print Job initialization', variable=p,onvalue="Print Job initialization",offvalue="").grid(row=8,column=0,sticky="w")

        1. WARNINGS, BED, ERRORS, FAILS, LEVEL OUTPUT, PRINT TIME, PRINT JOB INITIALAZATION
        """

        toplabel = QLabel("Markforged Log Parser")
        featurelabel = QLabel("Features")
        filterslabel = QLabel("Filters")
        # featurelabel.setTextAlignment(Qt.AlignRight)
        # filterslabel.setTextAlignment(Qt.AlignLeft)


        parsebutton = QPushButton("Parse Log")
        browsebutton = QPushButton("Browse")#browse button
        bedlevelbutton = QPushButton("Bed Leveling Data")
        quickinfolabel = QLabel("Quick Info:")
        printtimelabel = QLabel("print Time:")
        bedlevelingfilter = QCheckBox("Bed Leveling Data")
        warnings = QCheckBox("WARNINGS")
        BED = QCheckBox("BED")
        ERRORS = QCheckBox("ERRORS")
        FAILS = QCheckBox("FAILS")
        LEVELOUTPUT = QCheckBox("LEVEL OUTPUT")
        PRINTTIME = QCheckBox("PRINT TIME")
        PRINTJOB = QCheckBox("PRINT JOB INITIALIZATION")




        #defining first Hbox for welcome label -> stretch across top of program
        welcomehbox = QVBoxLayout()
        welcomehbox.addWidget(toplabel)


        titleshbox = QHBoxLayout()
        titleshbox.addWidget(filterslabel)
        titleshbox.addWidget(featurelabel)

        #define vbox for filters
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
        #define vbox for buttons
        buttonHbox = QVBoxLayout()
        buttonHbox.addWidget(browsebutton)
        buttonHbox.addWidget(parsebutton)
        buttonHbox.addWidget(bedlevelbutton)


        #define quick info hbox
        quickinfohbox = QHBoxLayout()
        quickinfohbox.addWidget(quickinfolabel)

        #define quick info info vbox
        quickinfoinfo = QVBoxLayout()
        quickinfoinfo.addWidget(printtimelabel) #this will need to be added to in order to display information

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