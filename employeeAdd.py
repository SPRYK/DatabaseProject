import EmployeeController, mysql.connector, datetime, addDoctorPopup
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(408, 667)
        self.male = QtWidgets.QRadioButton(self.Dialog)
        self.male.setGeometry(QtCore.QRect(140, 160, 95, 20))
        self.male.setObjectName("male")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 81, 20))
        self.label_3.setObjectName("label_3")
        self.DoB = QtWidgets.QDateEdit(self.Dialog)
        self.DoB.setGeometry(QtCore.QRect(150, 200, 110, 22))
        self.DoB.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.DoB.setCalendarPopup(True)
        self.DoB.setTimeSpec(QtCore.Qt.LocalTime)
        self.DoB.setDate(QtCore.QDate(2000, 1, 2))
        self.DoB.setObjectName("DoB")
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
        self.eid = QtWidgets.QLineEdit(self.Dialog)
        self.eid.setGeometry(QtCore.QRect(140, 30, 171, 22))
        self.eid.setObjectName("eid")
        self.female = QtWidgets.QRadioButton(self.Dialog)
        self.female.setGeometry(QtCore.QRect(250, 160, 95, 20))
        self.female.setObjectName("female")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(130, 70, 171, 22))
        self.name.setObjectName("name")
        self.nid = QtWidgets.QLineEdit(self.Dialog)
        self.nid.setGeometry(QtCore.QRect(130, 110, 171, 22))
        self.nid.setObjectName("nid")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(200, 610, 93, 28))
        self.cancel.setObjectName("cancel")
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(50, 610, 93, 28))
        self.ok.setObjectName("ok")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 71, 20))
        self.label_6.setObjectName("label_6")
        self.joinDate = QtWidgets.QDateEdit(self.Dialog)
        self.joinDate.setGeometry(QtCore.QRect(150, 240, 110, 22))
        self.joinDate.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.joinDate.setCalendarPopup(True)
        self.joinDate.setTimeSpec(QtCore.Qt.LocalTime)
        self.joinDate.setDate(QtCore.QDate(2000, 1, 2))
        self.joinDate.setObjectName("joinDate")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 290, 61, 20))
        self.label_7.setObjectName("label_7")
        self.salary = QtWidgets.QLineEdit(self.Dialog)
        self.salary.setGeometry(QtCore.QRect(130, 290, 171, 22))
        self.salary.setObjectName("salary")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 340, 121, 20))
        self.label_8.setObjectName("label_8")
        self.department = QtWidgets.QComboBox(self.Dialog)
        self.department.setGeometry(QtCore.QRect(160, 340, 141, 22))
        self.department.setObjectName("department")
        self.label_9 = QtWidgets.QLabel(self.Dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 390, 71, 20))
        self.label_9.setObjectName("label_9")
        self.job = QtWidgets.QComboBox(self.Dialog)
        self.job.setGeometry(QtCore.QRect(160, 390, 141, 22))
        self.job.setObjectName("job")
        self.phone = QtWidgets.QLineEdit(self.Dialog)
        self.phone.setGeometry(QtCore.QRect(133, 480, 171, 22))
        self.phone.setObjectName("phone")
        self.label_10 = QtWidgets.QLabel(self.Dialog)
        self.label_10.setGeometry(QtCore.QRect(177, 450, 61, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Dialog)
        self.label_11.setGeometry(QtCore.QRect(80, 480, 61, 20))
        self.label_11.setObjectName("label_11")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(40, 460, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            sqlQuery = "select * from "+"department"

            cursor = connection.cursor(buffered=True)
            cursor.execute(sqlQuery)
            records = cursor.fetchall()
                    
        except:
            retmsg = ["1", "Fetch Error"]
        else :
            retmsg = ["1", "Empty"]
            try:
                if records[0] != "" :
                    retmsg = ["0", "Found"]
            except:
                pass
        finally:
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                if(retmsg[0]=='0') :
                    self.department.addItem("")
                    for dept in records:
                        self.department.addItem(str(dept[0]))
                    self.job.addItem("")
                    self.job.addItem("Doctor")
                    self.job.addItem("Nurse")
                    self.job.addItem("Other")
            except:
                pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.male.setText(_translate("Dialog", "Male"))
        self.label_3.setText(_translate("Dialog", "Personal ID :"))
        self.label_2.setText(_translate("Dialog", "Name :"))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        self.label.setText(_translate("Dialog", "Employee ID :"))
        self.label_5.setText(_translate("Dialog", "Birth Date :"))
        self.female.setText(_translate("Dialog", "Female"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.label_6.setText(_translate("Dialog", "Join Date :"))
        self.label_7.setText(_translate("Dialog", "Salary :"))
        self.label_8.setText(_translate("Dialog", "Select Department :"))
        self.label_9.setText(_translate("Dialog", "Job Type :"))
        self.label_10.setText(_translate("Dialog", "Multivalue"))
        self.label_11.setText(_translate("Dialog", "Phone :"))


    def show(self):
        self.Dialog.show()

    def add(self):
        employID = self.eid.text()
        name = self.name.text()
        personalID = self.nid.text()
        gender = ""
        if self.male.isChecked():
            gender = "Male"
        elif self.female.isChecked():
            gender = "Female"
        birthDate = datetime.date(int(self.DoB.date().year()), int(self.DoB.date().month()), int(self.DoB.date().day()))
        joinDate = datetime.date(int(self.joinDate.date().year()), int(self.joinDate.date().month()), int(self.joinDate.date().day()))
        salary = self.salary.text()
        department = str(self.department.currentText())
        job = str(self.job.currentText())
        phones = self.phone.text()

        if(job == "Doctor"):
            job = "1"
        elif(job == "Nurse"):
            job = "2"
        elif(job == "Other"):
            job = "3"

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (employID, personalID, name, gender, birthDate, department, joinDate, salary, job)
            
            sqlQuery = "insert into "+"employee"+"(Employee_ID, Employee_NID, Employee_Name, Employee_Gender, Employee_DoB, Dept_ID, Join_Date, Salarly, Job_Type) " \
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            temp_list = list(objdata)


            if(name == ""):
                temp_list.remove(name)
                sqlQuery=sqlQuery.replace(" Employee_Name,",'')
                sqlQuery=sqlQuery.replace("%s,",'',1)
            if(gender == ""):
                temp_list.remove(gender)
                sqlQuery=sqlQuery.replace(" Employee_Gender,",'')
                sqlQuery=sqlQuery.replace("%s,",'',1)
            if(department == ""):
                temp_list.remove(department)
                sqlQuery=sqlQuery.replace(" Dept_ID,",'')
                sqlQuery=sqlQuery.replace("%s,",'',1)
            if(salary == ""):
                temp_list.remove(salary)
                sqlQuery=sqlQuery.replace(" Salarly,",'')
                sqlQuery=sqlQuery.replace("%s,",'',1)
            if(job == ""):
                temp_list.remove(job)
                sqlQuery=sqlQuery.replace(", Job_Type",'')
                sqlQuery=sqlQuery.replace("%s,",'',1)

            objdata = tuple(temp_list)
            
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

        if(job == "1"):
            self.ui = addDoctorPopup.Ui_Dialog(employID,
                                               name,
                                               personalID,
                                               gender,
                                               birthDate,
                                               joinDate,
                                               salary, 
                                               department,
                                               phones)
            self.Dialog.close()
            self.ui.show()
        if(job == "2"):
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='hospital',
                                                     user='root',
                                                     password='root')
                objdata = (employID,)
                
                sqlQuery = "insert into "+"nurse"+"(Employee_ID) " \
                                "values(%s)"
                
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

        try:
            connection = mysql.connector.connect(host='localhost',database='hospital',user='root',password='root')
            sqlQuery = "insert into "+"employee_phone"+"(Employee_ID, Phone) "+"values(%s,%s)"

            for phone in phones.split():
                objdata = (employID,phone)
                cursor = connection.cursor()
                cursor.execute(sqlQuery, objdata)
                connection.commit()
            
        except:
            retmsg_s = ["1", "writing error"]
        else :
            retmsg_s = ["0", "writing done"]
        finally :
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
            except:
                pass
       
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
