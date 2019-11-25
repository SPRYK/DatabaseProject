from PyQt5 import QtCore, QtGui, QtWidgets
import EmployeeController
import mysql.connector
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(447, 441)
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 141, 20))
        self.label.setObjectName("label")
        self.radioButton_2 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 180, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 130, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 41, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 180, 51, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 81, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 90, 171, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.radioButton = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton.setGeometry(QtCore.QRect(150, 180, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 270, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_9 = QtWidgets.QLabel(self.Dialog)
        self.label_9.setGeometry(QtCore.QRect(80, 320, 71, 20))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(70, 220, 61, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 220, 171, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 270, 121, 20))
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 320, 141, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100-50, 390, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250+50, 390, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(250-75, 390, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.fill)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Edit by Employee ID :"))
        self.radioButton_2.setText(_translate("Dialog", "Female"))
        self.label_2.setText(_translate("Dialog", "Name :"))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        self.label_3.setText(_translate("Dialog", "Personal ID :"))
        self.radioButton.setText(_translate("Dialog", "Male"))
        self.label_9.setText(_translate("Dialog", "Job Type :"))
        self.label_7.setText(_translate("Dialog", "Salary :"))
        self.label_8.setText(_translate("Dialog", "Select Department :"))
        self.pushButton.setText(_translate("Dialog", "Edit"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Fill"))

    def show(self):
        self.Dialog.show()
        
    def fill(self):
        employeeID = self.lineEdit.text()
        #TODO add employee to self.textBrower
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (employeeID,)
            sqlQuery = "select * from "+"employee"+" where Employee_ID = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
                    
        except Exception as e:
            retmsg = ["1", "Error"]
            print(e)
            print("Error 1")
        else :
            retmsg = ["1", "Not Found"]
            try:
                if records[0] != "" :
                    retmsg = ["0", "Found"]
            except Exception as e:
                print(e)
        finally:
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                if(retmsg[0]=='1') :
                    a=1
                else :
                    self.lineEdit_4.setText(str(records[2]))
                    self.lineEdit_3.setText(str(records[1]))
                    self.lineEdit_5.setText(str(records[7]))
                    if(records[3]=="Male"):
                        self.radioButton.setChecked(True)
                    else:
                        self.radioButton_2.setChecked(True)
                    index_2 = self.comboBox_2.findText(str(records[5]), QtCore.Qt.MatchFixedString)
                    if(index_2==-1):
                        self.comboBox_2.addItem(str(records[5]))
                    self.comboBox_2.setCurrentIndex(self.comboBox_2.findText(str(records[5]), QtCore.Qt.MatchFixedString))
                    
                    index_3 = self.comboBox_3.findText(str(records[8]), QtCore.Qt.MatchFixedString)
                    if(index_3==-1):
                        self.comboBox_3.addItem(str(records[8]))
                    self.comboBox_3.setCurrentIndex(self.comboBox_3.findText(str(records[8]), QtCore.Qt.MatchFixedString))
                    
            except Exception as e:
                print(e) 

    def back(self):
        self.ui = EmployeeController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def edit(self):
        employeeID = self.lineEdit.text()
        name = self.lineEdit_4.text()
        personalID = self.lineEdit_3.text()
        salary = self.lineEdit_5.text()
        gender = ""
        if self.radioButton.isChecked():
            gender = "Male"
        elif self.radioButton_2.isChecked():
            gender = "Female"
        department = str(self.comboBox_2.currentText())
        job = str(self.comboBox_3.currentText())
        #TODO edit name personalID salary gender department job by employeeID
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (employeeID,)
            sqlQuery = "select * from "+"employee"+" where Employee_ID = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
                    
        except Exception as e:
            retmsg = ["1", "Error"]
            print(e)
            print("Erorr 1")
        else :
            retmsg = ["1", "Not Found"]
            try:
                if records[0] != "" :
                    try:
                        sqlQuery = "update employee set Employee_Name = %s, Employee_NID = %s, Employee_Gender = %s, Salarly = %s, Dept_ID = %s, Job_Type = %s where Employee_ID = %s"
                        objdata = (name,personalID,gender,salary,department,job,employeeID)
                        
                        cursor = connection.cursor()
                        cursor.execute(sqlQuery, objdata)
                        connection.commit()
                        retmsg = ["0", "Edited"]
                    except Exception as e:
                        retmsg = ["1", "Error"]
                        print(e)
                        print("Erorr 3")
            except Exception as e:
                print(e)
                print("Erorr 2")
        finally:
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
            except Exception as e:
                print(e)
                print("Erorr 4")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
