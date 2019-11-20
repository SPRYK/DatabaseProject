# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appointmentEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import DepartmentController


class Ui_Dialog(object):
    
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 386)
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 121, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 310, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 111, 20))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 180, 171, 87))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 310, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(190, 90, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 151, 20))
        self.label_5.setObjectName("label_5")
        self.timeEdit = QtWidgets.QTimeEdit(self.Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(190, 140, 118, 22))
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 141, 20))
        self.label.setObjectName("label")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.cancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Appointment Time :"))
        self.pushButton.setText(_translate("Dialog", "Edit"))
        self.label_2.setText(_translate("Dialog", "Appointment Date :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_5.setText(_translate("Dialog", "Appointment Description :"))
        self.label.setText(_translate("Dialog", "Edit by Appointment ID :"))

    def show(self):
        self.Dialog.show()

    def cancel(self):
        self.ui = DepartmentController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def edit(self):
        appointID = self.lineEdit.text()
        date = self.dateEdit.date()
        time = self.timeEdit.time()
        desc = self.plainTextEdit.toPlainText()
        #TODO edit by appointID

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
