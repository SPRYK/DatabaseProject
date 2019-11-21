from PyQt5 import QtCore, QtGui, QtWidgets
import ScheduleController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 530)
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 410, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 41, 20))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 131, 20))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(160, 70, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.Dialog)
        self.timeEdit_2.setGeometry(QtCore.QRect(230, 220, 61, 22))
        self.timeEdit_2.setCalendarPopup(False)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 220, 31, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 20, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 410, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.Dialog)
        self.textEdit.setGeometry(QtCore.QRect(150, 270, 161, 87))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 51, 20))
        self.label_2.setObjectName("label_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(120, 220, 61, 22))
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 130, 81, 20))
        self.label_7.setObjectName("label_7")
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.Dialog)
        self.timeEdit_3.setGeometry(QtCore.QRect(170, 130, 61, 22))
        self.timeEdit_3.setCalendarPopup(False)
        self.timeEdit_3.setObjectName("timeEdit_3")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.back)         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", " Employee ID :"))
        self.label_3.setText(_translate("Dialog", "Start :"))
        self.label_6.setText(_translate("Dialog", " Schedule Description :"))
        self.label_5.setText(_translate("Dialog", "To :"))
        self.pushButton.setText(_translate("Dialog", "Edit"))
        self.label_2.setText(_translate("Dialog", " Date :"))
        self.label_7.setText(_translate("Dialog", "Start Time :"))


    def show(self):
        self.Dialog.show()

    def edit(self):
        employID = self.lineEdit_2.text()
        scheduleDesc = self.textEdit.toPlainText()
        date = self.dateEdit.date()
        oldStart = self.timeEdit_3.time()
        newStart = self.timeEdit.time()
        newEnd = self.timeEdit_2.time()
        #TODO edit scheduleDesc start end by employID date oldStart
        
        #how to date...
        print(date.day())
        print(date.month())
        print(date.year())
        #how to time...
        print(oldStart.hour())
        print(newEnd.minute())

        
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
