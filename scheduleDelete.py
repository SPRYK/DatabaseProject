import ScheduleController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(358, 247)
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(190, 180, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 81, 20))
        self.label_3.setObjectName("label_3")
        self.workDate = QtWidgets.QDateEdit(self.Dialog)
        self.workDate.setGeometry(QtCore.QRect(150, 70, 110, 22))
        self.workDate.setCalendarPopup(True)
        self.workDate.setObjectName("workDate")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(140, 20, 171, 22))
        self.id.setObjectName("id")
        self.delete_2 = QtWidgets.QPushButton(self.Dialog)
        self.delete_2.setGeometry(QtCore.QRect(40, 180, 121, 28))
        self.delete_2.setObjectName("delete_2")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 51, 20))
        self.label_2.setObjectName("label_2")
        self.startTime = QtWidgets.QTimeEdit(self.Dialog)
        self.startTime.setGeometry(QtCore.QRect(170, 120, 61, 22))
        self.startTime.setCalendarPopup(False)
        self.startTime.setObjectName("startTime")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.delete_2.clicked.connect(self.delete)
        self.cancel.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", " Employee ID :"))
        self.label_3.setText(_translate("Dialog", "Start Time :"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.label_2.setText(_translate("Dialog", " Date :"))


    def show(self):
        self.Dialog.show()


    def delete(self):
        employID = self.id.text()
        date = self.workDate.date()
        start = self.startTime.time()
        #TODO delete this schedule in database
        
        #get date by...
        print(date.day())
        print(date.month())
        print(date.year())
        #get time by...
        print(start.hour())
        print(start.minute())

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
