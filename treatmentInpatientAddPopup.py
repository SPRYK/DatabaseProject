from PyQt5 import QtCore, QtGui, QtWidgets
import patientController

class Ui_Dialog(object):
    def __init__(self, patientID, treatmentID, arrivalDate,
                 emergencyLv, assignDoc, diagDisease, drug,
                 appointID):
        self.patientID = patientID
        self.treatmentID = treatmentID
        self.arrivalDate = arrivalDate
        self.emergencyLv = emergencyLv
        self.assignDoc = assignDoc
        self.diagDisease = diagDisease
        self.drug = drug
        self.appointID = appointID
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 368)
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(120, 20, 131, 20))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 70, 91, 20))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 70, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.radioButton_4 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(220, 120, 81, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 111, 20))
        self.label_7.setObjectName("label_7")
        self.radioButton_3 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 120, 51, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(310, 120, 81, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 111, 20))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(170, 160, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 290, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 290, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 220, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 220, 91, 20))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Inpatient Information"))
        self.label_6.setText(_translate("Dialog", "Choose Bed :"))
        self.radioButton_4.setText(_translate("Dialog", "Medium"))
        self.label_7.setText(_translate("Dialog", "Attention Level :"))
        self.radioButton_3.setText(_translate("Dialog", "High"))
        self.radioButton_5.setText(_translate("Dialog", "Low"))
        self.label_2.setText(_translate("Dialog", "Discharge Date :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.label_8.setText(_translate("Dialog", "Assign Nurse :"))

    def show(self):
        self.Dialog.show()

    def add(self):
        bed = str(self.comboBox.currentText())
        dischargeDate = self.dateEdit.date()
        attentionLv = ""
        if self.radioButton_3.isChecked():
            attentionLv = "High"
        elif self.radioButton_4.isChecked():
            attentionLv = "Medium"
        elif self.radioButton_5.isChecked():
            attentionLv = "Low"
        assignNurse = str(self.comboBox_2.currentText())
        #TODO add treatment(for inpatien) to database



        #get date by...
        print(dischargeDate.day())
        print(dischargeDate.month())
        print(dischargeDate.year())

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
