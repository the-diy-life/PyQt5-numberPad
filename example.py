# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/amrlsayed/qt_workspace/FeederDesigns/feederDesigns.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel,QWidget

from number_pad import numberPopup

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow") 
        #MainWindow.resize(400, 400)
        self.MainWindow.setGeometry(QtCore.QRect(0, 0, 800, 800))     
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setObjectName("lineEdit")  
        self.lineEdit.setGeometry(QtCore.QRect(130, 120, 200, 27))      

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 200, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.push_button_clicked)
        
        self.MainWindow.mouseReleaseEvent = self.onClick
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Trigger Numberpad"))
        self.lineEdit.setText(_translate("MainWindow", "Number:"))

    def push_button_clicked(self):
        self.MainWindow.setEnabled(False)
        self.exPopup = numberPopup(self.MainWindow,self.lineEdit, "Number:", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(130, 320,400, 300)
        self.exPopup.show()  

    def onClick(self,e):
        self.MainWindow.setEnabled(True)

    def callBackOnSubmit(self, arg1, arg2): 
        print("Function is called with args: %s & %s" % (arg1, arg2))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
