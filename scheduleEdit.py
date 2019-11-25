import ScheduleController
from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
password = 'meow'


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 530)
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(220, 440, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 41, 20))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 131, 20))
        self.label_6.setObjectName("label_6")
        self.workDate = QtWidgets.QDateEdit(self.Dialog)
        self.workDate.setGeometry(QtCore.QRect(160, 70, 110, 22))
        self.workDate.setCalendarPopup(True)
        self.workDate.setObjectName("workDate")
        self.newEndTime = QtWidgets.QTimeEdit(self.Dialog)
        self.newEndTime.setGeometry(QtCore.QRect(230, 220, 61, 22))
        self.newEndTime.setCalendarPopup(False)
        self.newEndTime.setObjectName("newEndTime")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 220, 31, 20))
        self.label_5.setObjectName("label_5")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(160, 20, 171, 22))
        self.id.setObjectName("id")
        self.edit = QtWidgets.QPushButton(self.Dialog)
        self.edit.setGeometry(QtCore.QRect(70, 440, 121, 28))
        self.edit.setObjectName("edit")
        self.newScheduleDes = QtWidgets.QTextEdit(self.Dialog)
        self.newScheduleDes.setGeometry(QtCore.QRect(150, 270, 161, 87))
        self.newScheduleDes.setObjectName("newScheduleDes")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 51, 20))
        self.label_2.setObjectName("label_2")
        self.newStartTime = QtWidgets.QTimeEdit(self.Dialog)
        self.newStartTime.setGeometry(QtCore.QRect(120, 220, 61, 22))
        self.newStartTime.setCalendarPopup(False)
        self.newStartTime.setObjectName("newStartTime")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 130, 81, 20))
        self.label_7.setObjectName("label_7")
        self.startTime = QtWidgets.QTimeEdit(self.Dialog)
        self.startTime.setGeometry(QtCore.QRect(170, 130, 61, 22))
        self.startTime.setCalendarPopup(False)
        self.startTime.setObjectName("startTime")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(40, 180, 341, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.edit.clicked.connect(self.editing)
        self.cancel.clicked.connect(self.back)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", " Employee ID :"))
        self.label_3.setText(_translate("Dialog", "Start :"))
        self.label_6.setText(_translate("Dialog", " Schedule Description :"))
        self.label_5.setText(_translate("Dialog", "To :"))
        self.edit.setText(_translate("Dialog", "Edit"))
        self.label_2.setText(_translate("Dialog", " Date :"))
        self.label_7.setText(_translate("Dialog", "Start Time :"))


    def show(self):
        self.Dialog.show()


    def editing(self):
        employID = self.id.text()
        scheduleDesc = self.newScheduleDes.toPlainText()
        date = self.workDate.date()
        oldStart = self.startTime.time()
        newStart = self.newStartTime.time()
        newEnd = self.newEndTime.time()
        #TODO edit schedule
        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('')
            print('executed')
            connection.commit()
            #result = cursor.fetchall()
            #print(result)
            connection.close()
        except Exception as e :
            print(e)
        #how to date...
        print(date.day())
        print(date.month())
        print(date.year())
        #how to time...
        print(oldStart.hour())
        print(newEnd.minute())


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
