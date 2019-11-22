from PyQt5 import QtCore, QtGui, QtWidgets
import patientController, treatmentInpatientAddPopup

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(505, 436)
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 60, 91, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 60, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 380, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 380, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 20, 71, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 20, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 111, 20))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(200, 100, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.radioButton_4 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(230, 150, 81, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 150, 111, 20))
        self.label_6.setObjectName("label_6")
        self.radioButton_5 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(320, 150, 81, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(160, 150, 51, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 190, 91, 20))
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 190, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_9 = QtWidgets.QLabel(self.Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 230, 121, 20))
        self.label_9.setObjectName("label_9")
        self.comboBox_3 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 230, 141, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_10 = QtWidgets.QLabel(self.Dialog)
        self.label_10.setGeometry(QtCore.QRect(100, 270, 71, 20))
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(180, 270, 141, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(340, 210, 171, 16))
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(self.Dialog)
        self.label_11.setGeometry(QtCore.QRect(70, 320, 101, 20))
        self.label_11.setObjectName("label_11")
        self.comboBox_5 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(180, 320, 141, 22))
        self.comboBox_5.setObjectName("comboBox_5")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Treatment ID :"))
        self.pushButton.setText(_translate("Dialog", "Make Treatment"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_5.setText(_translate("Dialog", " Patient ID :"))
        self.label_2.setText(_translate("Dialog", "Arrival Date :"))
        self.radioButton_4.setText(_translate("Dialog", "Medium"))
        self.label_6.setText(_translate("Dialog", "Emergency Level :"))
        self.radioButton_5.setText(_translate("Dialog", "Low"))
        self.radioButton_3.setText(_translate("Dialog", "High"))
        self.label_8.setText(_translate("Dialog", "Assign Doctor :"))
        self.label_9.setText(_translate("Dialog", "Diagnose Disease :"))
        self.label_10.setText(_translate("Dialog", "Use Drug :"))
        self.label.setText(_translate("Dialog", "ต้องเปลี่ยนให้รับหลายอันได้"))
        self.label_11.setText(_translate("Dialog", "Appointment ID :"))
        

    def show(self):
        self.Dialog.show()

    def add(self):
        patientID = self.lineEdit_3.text()
        treatmentID = self.lineEdit_2.text()
        arrivalDate = self.dateEdit.date()
        emergencyLv = ""
        if self.radioButton_3.isChecked():
            emergencyLv = "High"
        elif self.radioButton_4.isChecked():
            emergencyLv = "Medium"
        elif self.radioButton_5.isChecked():
            emergencyLv = "Low"
        assignDoc = str(self.comboBox_2.currentText())
        diagDisease = str(self.comboBox_3.currentText())
        drug = str(self.comboBox_4.currentText())
        appointID = str(self.comboBox_5.currentText())

        if treatmentID.upper().startswith("I"):
            self.ui = treatmentInpatientAddPopup.Ui_Dialog(patientID,
                                               treatmentID,
                                               arrivalDate,
                                               emergencyLv,
                                               assignDoc,
                                               diagDisease,
                                               drug, 
                                               appointID)
            self.Dialog.hide()
            self.ui.show()
        else:        
            #TODO add treatment to database



            #get date by...
            print(arrivalDate.day())
            print(arrivalDate.month())
            print(arrivalDate.year())

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
