# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scheduleAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import ScheduleController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(398, 376)
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 20, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 51, 20))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(140, 70, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(120, 120, 61, 22))
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 41, 20))
        self.label_3.setObjectName("label_3")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.Dialog)
        self.timeEdit_2.setGeometry(QtCore.QRect(230, 120, 61, 22))
        self.timeEdit_2.setCalendarPopup(False)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 120, 31, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 310, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 310, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.Dialog)
        self.textEdit.setGeometry(QtCore.QRect(150, 170, 161, 87))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 131, 20))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", " Employee ID :"))
        self.label_2.setText(_translate("Dialog", " Date :"))
        self.label_3.setText(_translate("Dialog", "Start :"))
        self.label_5.setText(_translate("Dialog", "To :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Add Schedule"))
        self.label_6.setText(_translate("Dialog", " Schedule Description :"))


    def show(self):
        self.Dialog.show()

    def add(self):
        employID = self.lineEdit_2.text()
        scheduleDesc = self.textEdit.toPlainText()
        date = self.dateEdit.date()
        start = self.timeEdit.time()
        end = self.timeEdit_2.time()
        #TODO add new Schedule
        
        #get date by...
        print(date.day())
        print(date.month())
        print(date.year())
        #get time by...
        print(start.hour())
        print(end.minute())

        
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
