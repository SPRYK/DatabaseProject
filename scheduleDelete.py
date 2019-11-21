from PyQt5 import QtCore, QtGui, QtWidgets
import ScheduleController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(358, 247)
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 180, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 81, 20))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(150, 70, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 20, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 180, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 51, 20))
        self.label_2.setObjectName("label_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(170, 120, 61, 22))
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.back)    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", " Employee ID :"))
        self.label_3.setText(_translate("Dialog", "Start Time :"))
        self.pushButton.setText(_translate("Dialog", "Delete"))
        self.label_2.setText(_translate("Dialog", " Date :"))


    def show(self):
        self.Dialog.show()

    def delete(self):
        employID = self.lineEdit_2.text()
        date = self.dateEdit.date()
        start = self.timeEdit.time()
        #TODO delete this schedule in database
        
        #get date by...
        print(date.day())
        print(date.month())
        print(date.year())
        #get time by...
        print(start.hour())
        print(start.minute())

        
    def back(self):
        self.ui = ScheduleController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
