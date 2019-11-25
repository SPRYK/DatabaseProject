import patientController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(419, 465)
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 121, 20))
        self.label_3.setObjectName("label_3")
        self.edit = QtWidgets.QPushButton(self.Dialog)
        self.edit.setGeometry(QtCore.QRect(110, 410, 121, 28))
        self.edit.setObjectName("edit")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 111, 20))
        self.label_2.setObjectName("label_2")
        self.appointDes = QtWidgets.QPlainTextEdit(self.Dialog)
        self.appointDes.setGeometry(QtCore.QRect(180, 280, 171, 87))
        self.appointDes.setObjectName("appointDes")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(260, 410, 93, 28))
        self.cancel.setObjectName("cancel")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(160, 40, 150, 22))
        self.id.setObjectName("id")
        self.newAppointDate = QtWidgets.QDateEdit(self.Dialog)
        self.newAppointDate.setGeometry(QtCore.QRect(190, 120, 110, 22))
        self.newAppointDate.setCalendarPopup(True)
        self.newAppointDate.setObjectName("newAppointDate")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 280, 151, 20))
        self.label_5.setObjectName("label_5")
        self.newAppointTime = QtWidgets.QTimeEdit(self.Dialog)
        self.newAppointTime.setGeometry(QtCore.QRect(190, 170, 118, 22))
        self.newAppointTime.setCalendarPopup(False)
        self.newAppointTime.setObjectName("newAppointTime")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 141, 20))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(40, 80, 361, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(320, 36, 93, 28))
        self.fillButton.setObjectName("fillButton")
        self.newDoctorList = QtWidgets.QComboBox(self.Dialog)
        self.newDoctorList.setGeometry(QtCore.QRect(180, 220, 141, 22))
        self.newDoctorList.setObjectName("newDoctorList")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 220, 121, 20))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.edit.clicked.connect(self.editing)
        self.cancel.clicked.connect(self.back)
        self.fillButton.clicked.connect(self.fill)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Appointment Time :"))
        self.edit.setText(_translate("Dialog", "Edit"))
        self.label_2.setText(_translate("Dialog", "Appointment Date :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_5.setText(_translate("Dialog", "Appointment Description :"))
        self.label.setText(_translate("Dialog", "Edit by Appointment ID :"))
        self.fillButton.setText(_translate("Dialog", "Fill"))
        self.label_8.setText(_translate("Dialog", "Select Doctor :"))


    def show(self):
        self.Dialog.show()


    def editing(self):
        appointID = self.id.text()
        date = self.newAppointDate.date()
        time = self.newAppointTime.time()
        desc = self.appointDes.toPlainText()
        doctor = str(self.newDoctorList.currentText())
        #TODO edit by appointment

        self.ui = patientController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def fill(self):
        appointID = self.id.text()
        #TODO fill data

        
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
