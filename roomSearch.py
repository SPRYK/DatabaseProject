# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roomSearch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import RoomController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 30, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(190, 120, 161, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 161, 20))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 141, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "Search by Room ID :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Selected Department :"))


    def show(self):
        self.Dialog.show()

    def search(self):
        roomID = self.lineEdit.text()
        #TODO add room to self.textBrowser

        #example
        self.textBrowser.append("room1")
        self.textBrowser.append("room2")
        self.textBrowser.append("room3")
        
        

    def back(self):
        self.ui = RoomController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()         
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
