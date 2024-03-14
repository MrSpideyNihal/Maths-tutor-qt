#This code belongs to Nihal Rodge

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 756)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(" background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3b8d99, stop:0.5 #6b6b83, stop:1 #aa4b6b);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 580, 901, 121))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: white;background-color: transparent;")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(3)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 911, 71))

        #buttons 
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color:white;background-color: transparent;")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 720, 93, 28))
        self.pushButton.setStyleSheet(" background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 165, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 9px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 720, 93, 28))
        self.pushButton_2.setStyleSheet(" background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 165, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 9px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 720, 93, 28))
        self.pushButton_3.setStyleSheet(" background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 165, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 9px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 720, 93, 28))
        self.pushButton_4.setStyleSheet(" background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 165, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 9px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 290, 311, 281))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("welcome-2.gif"))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(370, 180, 221, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#on click .....
        self.pushButton.clicked.connect(self.show_msg)
        self.pushButton_2.clicked.connect(self.show_msg)
        self.pushButton_3.clicked.connect(self.show_msg)
        self.pushButton_4.clicked.connect(self.show_msg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Note: Adjust the speech rate by pressing the apostrophe or semicolon key, which are located to the left of the Enter<br>  key. Use the Space key to replay the question, and employ the Shift key to hear the question in verbose mode. Utilize<br>  settings to change arithmetic operation, difficulty, load questions, speech language, voice, etc. Press Alt+S to open<br>  or hide settings."))
        self.label_3.setText(_translate("MainWindow", "Welcome! Press enter to start"))
        self.pushButton.setText(_translate("MainWindow", "Show Settings"))
        self.pushButton_2.setText(_translate("MainWindow", "About"))
        self.pushButton_3.setText(_translate("MainWindow", "Help"))
        self.pushButton_4.setText(_translate("MainWindow", "Quit"))

#event handling..functions
    def show_msg(self):
        print("Button is Clicked!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
