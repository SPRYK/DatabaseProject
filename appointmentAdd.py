from PyQt5 import QtCore, QtGui, QtWidgets
import patientController


class Ui_Dialog(object):
        
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(414, 394)
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 330, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 330, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 101, 20))
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(170, 110, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(170, 160, 118, 22))
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 121, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 20, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 71, 20))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 200, 171, 87))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 151, 20))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Make Appointment"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Appointment ID :"))
        self.label_2.setText(_translate("Dialog", "Appointment Date :"))
        self.label_3.setText(_translate("Dialog", "Appointment Time :"))
        self.label_4.setText(_translate("Dialog", " Patient ID :"))
        self.label_5.setText(_translate("Dialog", "Appointment Description :"))
 
        

    def on_pushButton_clicked(self):
        patientID = self.lineEdit_2.text()
        appointID = self.lineEdit.text()
        date = self.dateEdit.date()
        time = self.timeEdit.time()
        desc = self.plainTextEdit.toPlainText()
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
        
        
    def on_pushButton_2_clicked(self):
        self.ui = patientController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def show(self):
        self.Dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
