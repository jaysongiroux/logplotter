import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication,QLabel)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        toplabel = QLabel("Markforged Log Parser")
        featurelabel = QLabel("Features")
        filterslabel = QLabel("Filters")
        parsebutton = QPushButton("Parse Log")
        browsebutton = QPushButton("Browse...")
        bedlevelbutton = QPushButton("Bed Leveling Data")
        quickinfolabel = QLabel("Quick Info:")

        #defining first Hbox for welcome label -> stretch across top of program
        welcomehbox = QHBoxLayout()
        welcomehbox.addStretch(0)
        welcomehbox.addWidget(toplabel)

        #define vbox for filters
        filtervbox = QVBoxLayout()
        filtervbox.addStretch(0)
        filtervbox.addWidget(filterslabel)
        """
        will need to add filters here
        """
        #define vbox for buttons
        buttonHbox = QHBoxLayout()
        buttonHbox.addStretch(0)
        buttonHbox.addWidget(browsebutton,parsebutton,bedlevelbutton)

        #define quick info hbox
        quickinfohbox = QHBoxLayout()
        quickinfohbox.addStretch(0)
        quickinfohbox.addWidget(quickinfolabel)

        #define quick info info vbox
        quickinfoinfo = QVBoxLayout()
        quickinfoinfo.addstretch(0)
        quickinfoinfo.addWidget() #this will need to be added to in order to display information

        #defining main container
        maincontainer = QVBoxLayout()
        maincontainer.addStretch(2)
        maincontainer.addWidget() #combines all of the together

        #defining vir box
        vbox = QVBoxLayout()
        vbox.addStretch(0)

        #adding hor box into ver box
        vbox.addLayout(hbox)
        vbox.addLayout(h2box)


        self.setLayout(vbox)


        #size of main window
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Log Plotter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())