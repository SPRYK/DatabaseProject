# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roomEdit.ui'
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
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(210, 100, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 100, 101, 20))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(90, 30, 111, 20))
        self.label.setObjectName("label")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Edit"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_7.setText(_translate("Dialog", "Room Type :"))
        self.label.setText(_translate("Dialog", "Edit by Room ID :"))

    def show(self):
        self.Dialog.show()

    def edit(self):
        roomID = self.lineEdit.text()
        roomType = str(self.comboBox.currentText())
        #TODO edit room by roomID
        
        

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
