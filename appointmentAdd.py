import patientController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(417, 487)
        self.makeAppoint = QtWidgets.QPushButton(self.Dialog)
        self.makeAppoint.setGeometry(QtCore.QRect(110, 430, 121, 28))
        self.makeAppoint.setObjectName("makeAppoint")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(260, 430, 93, 28))
        self.cancel.setObjectName("cancel")
        self.appointid = QtWidgets.QLineEdit(self.Dialog)
        self.appointid.setGeometry(QtCore.QRect(140, 60, 171, 22))
        self.appointid.setObjectName("appointid")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 101, 20))
        self.label.setObjectName("label")
        self.appointDate = QtWidgets.QDateEdit(self.Dialog)
        self.appointDate.setGeometry(QtCore.QRect(170, 110, 110, 22))
        self.appointDate.setCalendarPopup(True)
        self.appointDate.setObjectName("appointDate")
        self.appointTime = QtWidgets.QTimeEdit(self.Dialog)
        self.appointTime.setGeometry(QtCore.QRect(170, 160, 118, 22))
        self.appointTime.setCalendarPopup(False)
        self.appointTime.setObjectName("appointTime")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 121, 20))
        self.label_3.setObjectName("label_3")
        self.pid = QtWidgets.QLineEdit(self.Dialog)
        self.pid.setGeometry(QtCore.QRect(140, 20, 171, 22))
        self.pid.setObjectName("pid")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 71, 20))
        self.label_4.setObjectName("label_4")
        self.appointDes = QtWidgets.QPlainTextEdit(self.Dialog)
        self.appointDes.setGeometry(QtCore.QRect(180, 300, 171, 87))
        self.appointDes.setObjectName("appointDes")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 151, 20))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(70, 230, 121, 20))
        self.label_8.setObjectName("label_8")
        self.doctorList = QtWidgets.QComboBox(self.Dialog)
        self.doctorList.setGeometry(QtCore.QRect(170, 230, 141, 22))
        self.doctorList.setObjectName("doctorList")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.makeAppoint.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.makeAppoint.setText(_translate("Dialog", "Make Appointment"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Appointment ID :"))
        self.label_2.setText(_translate("Dialog", "Appointment Date :"))
        self.label_3.setText(_translate("Dialog", "Appointment Time :"))
        self.label_4.setText(_translate("Dialog", " Patient ID :"))
        self.label_5.setText(_translate("Dialog", "Appointment Description :"))
        self.label_8.setText(_translate("Dialog", "Select Doctor :"))


    def show(self):
        self.Dialog.show()



    def add(self):
        patientID = self.pid.text()
        appointID = self.appointid.text()
        date = self.appointDate.date()
        time = self.appointTime.time()
        desc = self.appointDes.toPlainText()
        doctor = str(self.doctorList.currentText())
        #TODO add new appointment to database

        #how to date...
        print(date.day())
        print(date.month())
        print(date.year())

        #how to time...
        print(time.hour())
        print(time.minute())

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
