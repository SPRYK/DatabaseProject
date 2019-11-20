# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patientController.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import appointmentAdd,appointmentDelete,appointmentEdit,appointmentSearch
import patientAdd,patientDelete,patientEdit,patientSearch
import MainController


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(573, 496)
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 70, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 140, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 70, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 140, 141, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 230, 141, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 420, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 290, 141, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 230, 141, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 290, 141, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 230, 141, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(360, 290, 141, 28))
        self.pushButton_11.setObjectName("pushButton_11")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        
        self.pushButton.clicked.connect(self.add_patient)
        self.pushButton_2.clicked.connect(self.edit_patient)
        self.pushButton_3.clicked.connect(self.delete_patient)
        self.pushButton_4.clicked.connect(self.search_patient)
        self.pushButton_5.clicked.connect(self.make_appointment)
        self.pushButton_6.clicked.connect(self.back)
        self.pushButton_7.clicked.connect(self.get_treatment)
        self.pushButton_8.clicked.connect(self.cancel_appointment)
        self.pushButton_9.clicked.connect(self.delete_treatment)
        self.pushButton_10.clicked.connect(self.search_appointment)
        self.pushButton_11.clicked.connect(self.search_treatment)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Add New Patient"))
        self.pushButton_2.setText(_translate("Dialog", "Edit Patient"))
        self.pushButton_3.setText(_translate("Dialog", "Delete Patient"))
        self.pushButton_4.setText(_translate("Dialog", "Search Patient"))
        self.pushButton_5.setText(_translate("Dialog", "Make Appointment"))
        self.pushButton_6.setText(_translate("Dialog", "Back"))
        self.pushButton_7.setText(_translate("Dialog", "Get Treatment"))
        self.pushButton_8.setText(_translate("Dialog", "Cancel Appointment"))
        self.pushButton_9.setText(_translate("Dialog", "Delete Treatment"))
        self.pushButton_10.setText(_translate("Dialog", "Search Appointment"))
        self.pushButton_11.setText(_translate("Dialog", "Search Treatment"))

    def show(self):
        self.Dialog.show()

    def back(self):
        self.ui = MainController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def add_patient(self):
        self.ui = patientAdd.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
    
    def edit_patient(self):
        self.ui = patientEdit.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
    
    def delete_patient(self):
        self.ui = patientDelete.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
    
    def search_patient(self):
        self.ui = patientSearch.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
    
    def make_appointment(self):
        self.ui = appointmentAdd.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
    
    def get_treatment(self):
        return
    
    def cancel_appointment(self):
        self.ui = appointmentDelete.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
    
    def delete_treatment(self):
        return
    
    def search_appointment(self):
        self.ui = appointmentSearch.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
    
    def search_treatment(self):
        return
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
