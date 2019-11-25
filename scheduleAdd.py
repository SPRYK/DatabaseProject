import ScheduleController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(398, 376)
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(140, 20, 171, 22))
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 51, 20))
        self.label_2.setObjectName("label_2")
        self.workDate = QtWidgets.QDateEdit(self.Dialog)
        self.workDate.setGeometry(QtCore.QRect(140, 70, 110, 22))
        self.workDate.setCalendarPopup(True)
        self.workDate.setObjectName("workDate")
        self.startTime = QtWidgets.QTimeEdit(self.Dialog)
        self.startTime.setGeometry(QtCore.QRect(120, 120, 61, 22))
        self.startTime.setCalendarPopup(False)
        self.startTime.setObjectName("startTime")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 41, 20))
        self.label_3.setObjectName("label_3")
        self.endTime = QtWidgets.QTimeEdit(self.Dialog)
        self.endTime.setGeometry(QtCore.QRect(230, 120, 61, 22))
        self.endTime.setCalendarPopup(False)
        self.endTime.setObjectName("endTime")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 120, 31, 20))
        self.label_5.setObjectName("label_5")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(220, 310, 93, 28))
        self.cancel.setObjectName("cancel")
        self.addSchedule = QtWidgets.QPushButton(self.Dialog)
        self.addSchedule.setGeometry(QtCore.QRect(70, 310, 121, 28))
        self.addSchedule.setObjectName("addSchedule")
        self.description = QtWidgets.QTextEdit(self.Dialog)
        self.description.setGeometry(QtCore.QRect(150, 170, 161, 87))
        self.description.setObjectName("description")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 131, 20))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.addSchedule.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", " Employee ID :"))
        self.label_2.setText(_translate("Dialog", " Date :"))
        self.label_3.setText(_translate("Dialog", "Start :"))
        self.label_5.setText(_translate("Dialog", "To :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.addSchedule.setText(_translate("Dialog", "Add Schedule"))
        self.label_6.setText(_translate("Dialog", " Schedule Description :"))


    def show(self):
        self.Dialog.show()

    def add(self):
        employID = self.id.text()
        scheduleDesc = self.description.toPlainText()
        date = self.startTime.date()
        start = self.timeEdit.time()
        end = self.endTime.time()
        #TODO add new Schedule
        
        #get date by...
        print(date.day())
        print(date.month())
        print(date.year())
        #get time by...
        print(start.hour())
        print(end.minute())


        self.ui = ScheduleController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()        
        
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
