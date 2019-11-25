import patientController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self, patientID, treatmentID, arrivalDate, emergencyLv, assignDoc, diagDisease, drug, appointID, symptom):
        self.patientID = patientID
        self.treatmentID = treatmentID
        self.arrivalDate = arrivalDate
        self.emergencyLv = emergencyLv
        self.assignDoc = assignDoc
        self.diagDisease = diagDisease
        self.drug = drug
        self.appointID = appointID
        self.symptom = symptom.split()
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 447)
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(120, 20, 131, 20))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 70, 91, 20))
        self.label_6.setObjectName("label_6")
        self.bedList = QtWidgets.QComboBox(self.Dialog)
        self.bedList.setGeometry(QtCore.QRect(140, 70, 141, 22))
        self.bedList.setObjectName("bedList")
        self.attenMed = QtWidgets.QRadioButton(self.Dialog)
        self.attenMed.setGeometry(QtCore.QRect(220, 120, 81, 20))
        self.attenMed.setObjectName("attenMed")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 111, 20))
        self.label_7.setObjectName("label_7")
        self.attenHigh = QtWidgets.QRadioButton(self.Dialog)
        self.attenHigh.setGeometry(QtCore.QRect(150, 120, 51, 20))
        self.attenHigh.setObjectName("attenHigh")
        self.attenLow = QtWidgets.QRadioButton(self.Dialog)
        self.attenLow.setGeometry(QtCore.QRect(310, 120, 81, 20))
        self.attenLow.setObjectName("attenLow")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 111, 20))
        self.label_2.setObjectName("label_2")
        self.dischargeDate = QtWidgets.QDateEdit(self.Dialog)
        self.dischargeDate.setGeometry(QtCore.QRect(170, 160, 110, 22))
        self.dischargeDate.setCalendarPopup(True)
        self.dischargeDate.setObjectName("dischargeDate")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(210, 380, 93, 28))
        self.cancel.setObjectName("cancel")
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(60, 380, 121, 28))
        self.ok.setObjectName("ok")
        self.nurseList = QtWidgets.QComboBox(self.Dialog)
        self.nurseList.setGeometry(QtCore.QRect(150, 220, 141, 22))
        self.nurseList.setObjectName("nurseList")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 220, 91, 20))
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 61, 20))
        self.label_3.setObjectName("label_3")
        self.reason = QtWidgets.QLineEdit(self.Dialog)
        self.reason.setGeometry(QtCore.QRect(130, 290, 171, 22))
        self.reason.setObjectName("reason")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Inpatient Information"))
        self.label_6.setText(_translate("Dialog", "Choose Bed :"))
        self.attenMed.setText(_translate("Dialog", "Medium"))
        self.label_7.setText(_translate("Dialog", "Attention Level :"))
        self.attenHigh.setText(_translate("Dialog", "High"))
        self.attenLow.setText(_translate("Dialog", "Low"))
        self.label_2.setText(_translate("Dialog", "Discharge Date :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.label_8.setText(_translate("Dialog", "Assign Nurse :"))
        self.label_3.setText(_translate("Dialog", "Reason :"))


    def show(self):
        self.Dialog.show()


    def add(self):
        bed = str(self.bedList.currentText())
        dischargeDate = self.dischargeDate.date()
        attentionLv = ""
        if self.attenHigh.isChecked():
            attentionLv = "High"
        elif self.attenMed.isChecked():
            attentionLv = "Medium"
        elif self.attenLow.isChecked():
            attentionLv = "Low"
        assignNurse = str(self.nurseList.currentText())
        reason = self.reason.text()        
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
