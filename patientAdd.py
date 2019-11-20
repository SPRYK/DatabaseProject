# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patientAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import patientController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(502, 464)
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 71, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 41, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 70, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 81, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 110, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 51, 20))
        self.label_4.setObjectName("label_4")

        self.gender_group=QtWidgets.QButtonGroup(self.Dialog)
        
        self.radioButton = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton.setGeometry(QtCore.QRect(160, 160, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 160, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        self.gender_group.addButton(self.radioButton)
        self.gender_group.addButton(self.radioButton_2)

        
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 200, 71, 20))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(170, 200, 110, 22))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setDate(QtCore.QDate(2000, 1, 2))
        self.dateEdit.setObjectName("dateEdit")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 240, 81, 20))
        self.label_6.setObjectName("label_6")

        self.blood_group=QtWidgets.QButtonGroup(self.Dialog)
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(160, 240, 51, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(210, 240, 41, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(260, 240, 41, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(300, 240, 41, 20))
        self.radioButton_6.setObjectName("radioButton_6")

        self.blood_group.addButton(self.radioButton_3)
        self.blood_group.addButton(self.radioButton_4)
        self.blood_group.addButton(self.radioButton_5)
        self.blood_group.addButton(self.radioButton_6)
        
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 400, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 320, 51, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 320, 171, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 280, 61, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 280, 171, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Patient ID :"))
        self.label_2.setText(_translate("Dialog", "Name :"))
        self.label_3.setText(_translate("Dialog", "Personal ID :"))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        self.radioButton.setText(_translate("Dialog", "Male"))
        self.radioButton_2.setText(_translate("Dialog", "Female"))
        self.label_5.setText(_translate("Dialog", "Birth Date :"))
        self.label_6.setText(_translate("Dialog", "Blood Group :"))
        self.radioButton_3.setText(_translate("Dialog", "O"))
        self.radioButton_4.setText(_translate("Dialog", "A"))
        self.radioButton_5.setText(_translate("Dialog", "B"))
        self.radioButton_6.setText(_translate("Dialog", "AB"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_7.setText(_translate("Dialog", "Phone :"))
        self.label_8.setText(_translate("Dialog", "Allergic :"))

    def show(self):
        self.Dialog.show()

    def add(self):
        gender = ""
        blood = ""
        if self.radioButton.isChecked():
            gender = "Male"
        elif self.radioButton_2.isChecked():
            gender = "Female"
        if self.radioButton_3.isChecked():
            blood = "O"
        elif self.radioButton_4.isChecked():
            blood = "A"
        elif self.radioButton_5.isChecked():
            blood = "B"
        elif self.radioButton_6.isChecked():
            blood = "AB"
        patientID = self.lineEdit.text()
        name = self.lineEdit_2.text()
        personalID = self.lineEdit_3.text()
        birthDate = self.dateEdit.date()
        allergic = self.lineEdit_5.text()
        phone =  self.lineEdit_4.text()
        #TODO add new patient

        
        #get date by...
        print(birthDate.day())
        print(birthDate.month())
        print(birthDate.year())

        
    def back(self):
        self.ui = patientController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
