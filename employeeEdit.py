import EmployeeController, mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(488, 568)
        self.eid = QtWidgets.QLineEdit(self.Dialog)
        self.eid.setGeometry(QtCore.QRect(190, 30, 161, 22))
        self.eid.setObjectName("eid")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 141, 20))
        self.label.setObjectName("label")
        self.female = QtWidgets.QRadioButton(self.Dialog)
        self.female.setGeometry(QtCore.QRect(260, 180, 95, 20))
        self.female.setObjectName("female")
        self.nid = QtWidgets.QLineEdit(self.Dialog)
        self.nid.setGeometry(QtCore.QRect(140, 130, 171, 22))
        self.nid.setObjectName("nid")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 41, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 180, 51, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 81, 20))
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(140, 90, 171, 22))
        self.name.setObjectName("name")
        self.male = QtWidgets.QRadioButton(self.Dialog)
        self.male.setGeometry(QtCore.QRect(150, 180, 95, 20))
        self.male.setObjectName("male")
        self.department = QtWidgets.QComboBox(self.Dialog)
        self.department.setGeometry(QtCore.QRect(170, 270, 141, 22))
        self.department.setObjectName("department")
        self.label_9 = QtWidgets.QLabel(self.Dialog)
        self.label_9.setGeometry(QtCore.QRect(80, 320, 71, 20))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(70, 220, 61, 20))
        self.label_7.setObjectName("label_7")
        self.salary = QtWidgets.QLineEdit(self.Dialog)
        self.salary.setGeometry(QtCore.QRect(140, 220, 171, 22))
        self.salary.setObjectName("salary")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 270, 121, 20))
        self.label_8.setObjectName("label_8")
        self.job = QtWidgets.QComboBox(self.Dialog)
        self.job.setGeometry(QtCore.QRect(170, 320, 141, 22))
        self.job.setObjectName("job")
        self.edit = QtWidgets.QPushButton(self.Dialog)
        self.edit.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.edit.setObjectName("edit")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(250, 510, 93, 28))
        self.cancel.setObjectName("cancel")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(40, 60, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(370, 30, 93, 28))
        self.fillButton.setObjectName("fillButton")
        self.label_10 = QtWidgets.QLabel(self.Dialog)
        self.label_10.setGeometry(QtCore.QRect(187, 390, 61, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Dialog)
        self.label_11.setGeometry(QtCore.QRect(90, 420, 61, 20))
        self.label_11.setObjectName("label_11")
        self.phone = QtWidgets.QLineEdit(self.Dialog)
        self.phone.setGeometry(QtCore.QRect(143, 420, 171, 22))
        self.phone.setObjectName("phone")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(50, 400, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.edit.clicked.connect(self.editing)
        self.cancel.clicked.connect(self.back)
        self.fillButton.clicked.connect(self.fill)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Edit by Employee ID :"))
        self.female.setText(_translate("Dialog", "Female"))
        self.label_2.setText(_translate("Dialog", "Name :"))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        self.label_3.setText(_translate("Dialog", "Personal ID :"))
        self.male.setText(_translate("Dialog", "Male"))
        self.label_9.setText(_translate("Dialog", "Job Type :"))
        self.label_7.setText(_translate("Dialog", "Salary :"))
        self.label_8.setText(_translate("Dialog", "Select Department :"))
        self.edit.setText(_translate("Dialog", "Edit"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.fillButton.setText(_translate("Dialog", "Fill"))
        self.label_10.setText(_translate("Dialog", "Multivalue"))
        self.label_11.setText(_translate("Dialog", "Phone :"))


    def show(self):
        self.Dialog.show()


    def fill(self):
        employeeID = self.eid.text()
        
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
                if(retmsg[0]!='1'):
                    self.name.setText(str(records[2]))
                    self.nid.setText(str(records[1]))
                    self.salary.setText(str(records[7]))
                    if(records[3]=="Male"):
                        self.male.setChecked(True)
                    else:
                        self.female.setChecked(True)
                    index_2 = self.department.findText(str(records[5]), QtCore.Qt.MatchFixedString)
                    if(index_2==-1):
                        self.department.addItem(str(records[5]))
                    self.department.setCurrentIndex(self.department.findText(str(records[5]), QtCore.Qt.MatchFixedString))
                    
                    index_3 = self.job.findText(str(records[8]), QtCore.Qt.MatchFixedString)
                    if(index_3==-1):
                        self.job.addItem(str(records[8]))
                    self.job.setCurrentIndex(self.job.findText(str(records[8]), QtCore.Qt.MatchFixedString))
                    #TODO fill phone

                    
            except Exception as e:
                print(e) 

    def back(self):
        self.ui = EmployeeController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        

    def editing(self):
        employeeID = self.eid.text()
        name = self.name.text()
        personalID = self.nid.text()
        salary = self.salary.text()
        gender = ""
        if self.male.isChecked():
            gender = "Male"
        elif self.female.isChecked():
            gender = "Female"
        department = str(self.department.currentText())
        job = str(self.job.currentText())
        
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
                        #TODO edit phone

                        
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
