from PyQt5 import QtCore, QtGui, QtWidgets
import patientController

class Ui_Dialog(object):
    def __init__(self,patientID, patientName, personalID,
                 birthDate, allergic, phone, gender, blood):
        self.patientID = patientID
        self.patientName = patientName
        self.personalID = personalID
        self.birthDate = birthDate
        self.allergic = allergic
        self.phone = phone
        self.gender = gender
        self.blood = blood
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 30, 91, 20))
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 180, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 180, 91, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 250, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 111, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 250, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(160, 80, 51, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(230, 80, 81, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(320, 80, 81, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 111, 20))
        self.label_7.setObjectName("label_7")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(180, 120, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Choose Bed :"))
        self.label_8.setText(_translate("Dialog", "Assign Nurse :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Discharge Date :"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.radioButton_3.setText(_translate("Dialog", "High"))
        self.radioButton_4.setText(_translate("Dialog", "Medium"))
        self.radioButton_5.setText(_translate("Dialog", "Low"))
        self.label_7.setText(_translate("Dialog", "Attention Level :"))


    def show(self):
        self.Dialog.show()

    def add(self):
        self.attentionLv = ""
        if self.radioButton_3.isChecked():
            self.attentionLv = "High"
        elif self.radioButton_4.isChecked():
            self.attentionLv = "Medium"
        elif self.radioButton_5.isChecked():
            self.attentionLv = "Low"
        self.nurse = str(self.comboBox_2.currentText())
        self.bed = str(self.comboBox.currentText())
        self.dischargeDate = self.dateEdit.date()
        #TODO add new inpatient to database
        
        

        #get date by...
        print(self.dischargeDate.day())
        print(self.dischargeDate.month())
        print(self.dischargeDate.year())

        self.ui = patientController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

            
        
    def back(self):
        self.ui = patientController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
