# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DepartmentController.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import appointmentAdd


class Ui_Dialog(object):
        
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.pushButton_6 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 250, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 30, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 100, 141, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 100, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.open_appointment_add)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_6.setText(_translate("Dialog", "Back"))
        self.pushButton_3.setText(_translate("Dialog", "Delete Department"))
        self.pushButton_4.setText(_translate("Dialog", "Search Department"))
        self.pushButton.setText(_translate("Dialog", "Add New Department"))
        self.pushButton_2.setText(_translate("Dialog", "Edit Department"))

    def open_appointment_add(self):
        self.ui = appointmentAdd.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def show(self):
        self.Dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
