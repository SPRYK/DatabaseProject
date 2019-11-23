from PyQt5 import QtCore, QtGui, QtWidgets
import EmployeeController
import mysql.connector
from mysql.connector import Error
import datetime

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(408, 534)
        self.radioButton = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton.setGeometry(QtCore.QRect(140, 160, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 81, 20))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(150, 200, 110, 22))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setDate(QtCore.QDate(2000, 1, 2))
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 41, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 160, 51, 20))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 81, 20))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 200, 71, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton_2 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 160, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 110, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 470, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 470, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 71, 20))
        self.label_6.setObjectName("label_6")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(150, 240, 110, 22))
        self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_2.setDate(QtCore.QDate(2000, 1, 2))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 290, 61, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 290, 171, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 340, 121, 20))
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 340, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_9 = QtWidgets.QLabel(self.Dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 390, 71, 20))
        self.label_9.setObjectName("label_9")
        self.comboBox_3 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 390, 141, 22))
        self.comboBox_3.setObjectName("comboBox_3")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton.setText(_translate("Dialog", "Male"))
        self.label_3.setText(_translate("Dialog", "Personal ID :"))
        self.label_2.setText(_translate("Dialog", "Name :"))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        self.label.setText(_translate("Dialog", "Employee ID :"))
        self.label_5.setText(_translate("Dialog", "Birth Date :"))
        self.radioButton_2.setText(_translate("Dialog", "Female"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.label_6.setText(_translate("Dialog", "Join Date :"))
        self.label_7.setText(_translate("Dialog", "Salary :"))
        self.label_8.setText(_translate("Dialog", "Select Department :"))
        self.label_9.setText(_translate("Dialog", "Job Type :"))


    def show(self):
        self.Dialog.show()


    def add(self):
        employID = self.lineEdit.text()
        name = self.lineEdit_2.text()
        personalID = self.lineEdit_3.text()
        gender = ""
        if self.radioButton.isChecked():
            gender = "Male"
        elif self.radioButton_2.isChecked():
            gender = "Female"
        try:
            birthDate = datetime.date(int(self.dateEdit.date().year()), int(self.dateEdit.date().month()), int(self.dateEdit.date().day()))
            joinDate = datetime.date(int(self.dateEdit_2.date().year()), int(self.dateEdit_2.date().month()), int(self.dateEdit_2.date().day()))
        except Exception as e:
            print(e)   
        salary = self.lineEdit_4.text()
        department = str(self.comboBox_2.currentText())
        job = str(self.comboBox_3.currentText())

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (employID, personalID, name, gender, birthDate, 7, joinDate, salary, 9)
            
            sqlQuery = "insert into "+"employee"+"(Employee_ID, Employee_NID, Employee_Name, Employee_Gender, Employee_DoB, Dept_ID, Join_Date, Salarly, Job_Type) " \
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
        except:
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                
        self.ui = EmployeeController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        
        return retmsg

        
    def back(self):
        self.ui = EmployeeController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())

