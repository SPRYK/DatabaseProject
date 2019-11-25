from PyQt5 import QtCore, QtGui, QtWidgets
import patientController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(443, 637)
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 71, 20))
        self.label.setObjectName("label")
        self.pid = QtWidgets.QLineEdit(self.Dialog)
        self.pid.setGeometry(QtCore.QRect(150, 30, 171, 22))
        self.pid.setObjectName("pid")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 91, 20))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(150, 70, 171, 22))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 81, 20))
        self.label_3.setObjectName("label_3")
        self.nid = QtWidgets.QLineEdit(self.Dialog)
        self.nid.setGeometry(QtCore.QRect(150, 110, 171, 22))
        self.nid.setObjectName("nid")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 51, 20))
        self.label_4.setObjectName("label_4")
        self.male = QtWidgets.QRadioButton(self.Dialog)
        self.male.setGeometry(QtCore.QRect(160, 160, 95, 20))
        self.male.setObjectName("male")
        self.buttonGroup = QtWidgets.QButtonGroup(self.Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.male)
        self.female = QtWidgets.QRadioButton(self.Dialog)
        self.female.setGeometry(QtCore.QRect(270, 160, 95, 20))
        self.female.setObjectName("female")
        self.buttonGroup.addButton(self.female)
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 200, 71, 20))
        self.label_5.setObjectName("label_5")
        self.DoB = QtWidgets.QDateEdit(self.Dialog)
        self.DoB.setGeometry(QtCore.QRect(170, 200, 110, 22))
        self.DoB.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.DoB.setCalendarPopup(True)
        self.DoB.setTimeSpec(QtCore.Qt.LocalTime)
        self.DoB.setDate(QtCore.QDate(2000, 1, 2))
        self.DoB.setObjectName("DoB")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 240, 81, 20))
        self.label_6.setObjectName("label_6")
        self.bloodO = QtWidgets.QRadioButton(self.Dialog)
        self.bloodO.setGeometry(QtCore.QRect(160, 240, 51, 20))
        self.bloodO.setObjectName("bloodO")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(self.Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.bloodO)
        self.bloodA = QtWidgets.QRadioButton(self.Dialog)
        self.bloodA.setGeometry(QtCore.QRect(210, 240, 41, 20))
        self.bloodA.setObjectName("bloodA")
        self.buttonGroup_2.addButton(self.bloodA)
        self.bloodB = QtWidgets.QRadioButton(self.Dialog)
        self.bloodB.setGeometry(QtCore.QRect(260, 240, 41, 20))
        self.bloodB.setObjectName("bloodB")
        self.buttonGroup_2.addButton(self.bloodB)
        self.bloodAB = QtWidgets.QRadioButton(self.Dialog)
        self.bloodAB.setGeometry(QtCore.QRect(300, 240, 41, 20))
        self.bloodAB.setObjectName("bloodAB")
        self.buttonGroup_2.addButton(self.bloodAB)
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(80, 580, 93, 28))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(230, 580, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 460, 51, 20))
        self.label_7.setObjectName("label_7")
        self.phone = QtWidgets.QLineEdit(self.Dialog)
        self.phone.setGeometry(QtCore.QRect(150, 460, 171, 22))
        self.phone.setObjectName("phone")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 420, 61, 20))
        self.label_8.setObjectName("label_8")
        self.allergic = QtWidgets.QLineEdit(self.Dialog)
        self.allergic.setGeometry(QtCore.QRect(150, 420, 171, 22))
        self.allergic.setObjectName("allergic")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(57, 400, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(self.Dialog)
        self.label_9.setGeometry(QtCore.QRect(194, 390, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Dialog)
        self.label_10.setGeometry(QtCore.QRect(90, 280, 51, 20))
        self.label_10.setObjectName("label_10")
        self.unknownStatus = QtWidgets.QRadioButton(self.Dialog)
        self.unknownStatus.setGeometry(QtCore.QRect(160, 280, 81, 20))
        self.unknownStatus.setObjectName("unknownStatus")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(self.Dialog)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.unknownStatus)
        self.dischargedStatus = QtWidgets.QRadioButton(self.Dialog)
        self.dischargedStatus.setGeometry(QtCore.QRect(270, 280, 95, 20))
        self.dischargedStatus.setObjectName("dischargedStatus")
        self.buttonGroup_3.addButton(self.dischargedStatus)
        self.admittedStatus = QtWidgets.QRadioButton(self.Dialog)
        self.admittedStatus.setGeometry(QtCore.QRect(160, 330, 81, 20))
        self.admittedStatus.setObjectName("admittedStatus")
        self.buttonGroup_3.addButton(self.admittedStatus)
        self.deceasedStatus = QtWidgets.QRadioButton(self.Dialog)
        self.deceasedStatus.setGeometry(QtCore.QRect(270, 330, 95, 20))
        self.deceasedStatus.setObjectName("deceasedStatus")
        self.buttonGroup_3.addButton(self.deceasedStatus)
        self.medhistory = QtWidgets.QLineEdit(self.Dialog)
        self.medhistory.setGeometry(QtCore.QRect(150, 500, 171, 22))
        self.medhistory.setObjectName("medhistory")
        self.label_11 = QtWidgets.QLabel(self.Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 500, 101, 20))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Patient ID :"))
        self.label_2.setText(_translate("Dialog", "Patient Name :"))
        self.label_3.setText(_translate("Dialog", "National ID :"))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        self.male.setText(_translate("Dialog", "Male"))
        self.female.setText(_translate("Dialog", "Female"))
        self.label_5.setText(_translate("Dialog", "Birth Date :"))
        self.label_6.setText(_translate("Dialog", "Blood Group :"))
        self.bloodO.setText(_translate("Dialog", "O"))
        self.bloodA.setText(_translate("Dialog", "A"))
        self.bloodB.setText(_translate("Dialog", "B"))
        self.bloodAB.setText(_translate("Dialog", "AB"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_7.setText(_translate("Dialog", "Phone :"))
        self.label_8.setText(_translate("Dialog", "Allergic :"))
        self.label_9.setText(_translate("Dialog", "Multivalue"))
        self.label_10.setText(_translate("Dialog", "Status :"))
        self.unknownStatus.setText(_translate("Dialog", "Unknown"))
        self.dischargedStatus.setText(_translate("Dialog", "Discharged"))
        self.admittedStatus.setText(_translate("Dialog", "Admitted"))
        self.deceasedStatus.setText(_translate("Dialog", "Deceased"))
        self.label_11.setText(_translate("Dialog", "Medical History :"))


    def show(self):
        self.Dialog.show()


    def add(self):
        gender = ""
        blood = ""
        status = ""
        if self.male.isChecked():
            gender = "Male"
        elif self.female.isChecked():
            gender = "Female"
        if self.bloodO.isChecked():
            blood = "O"
        elif self.bloodA.isChecked():
            blood = "A"
        elif self.bloodB.isChecked():
            blood = "B"
        elif self.bloodAB.isChecked():
            blood = "AB"
        if self.unknownStatus.isChecked():
            status = "Unknown"
        elif self.dischargedStatus.isChecked():
            status = "Discharged"
        elif self.admittedStatus.isChecked():
            status = "Admitted"
        elif self.deceasedStatus.isChecked():
            status = "Deceased"
        patientID = self.pid.text()
        name = self.name.text()
        personalID = self.nid.text()
        birthDate = self.DoB.date()
        allergic = self.allergic.text()
        phone =  self.phone.text()
        medHistory = self.medhistory.text()
        #TODO add new patient to database

            
        #get date by...
        print(birthDate.day())
        print(birthDate.month())
        print(birthDate.year())
        
        self.ui = patientController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        
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
