import EmployeeController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self, employID, name, personalID, gender, birthDate, joinDate, salary, department, phones):
        self.employID = employID
        self.name = name
        self.personalID = personalID
        self.gender= gender
        self.birthDate = birthDate
        self.joinDate = joinDate
        self.salary = salary
        self.department = department
        self.phones = phones
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(523, 354)
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(87, 40, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_10 = QtWidgets.QLabel(self.Dialog)
        self.label_10.setGeometry(QtCore.QRect(224, 30, 61, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Dialog)
        self.label_11.setGeometry(QtCore.QRect(120, 80, 61, 20))
        self.label_11.setObjectName("label_11")
        self.degreeDoctor = QtWidgets.QLineEdit(self.Dialog)
        self.degreeDoctor.setGeometry(QtCore.QRect(180, 80, 221, 61))
        self.degreeDoctor.setObjectName("degreeDoctor")
        self.label_12 = QtWidgets.QLabel(self.Dialog)
        self.label_12.setGeometry(QtCore.QRect(90, 170, 91, 20))
        self.label_12.setObjectName("label_12")
        self.certiDoctor = QtWidgets.QLineEdit(self.Dialog)
        self.certiDoctor.setGeometry(QtCore.QRect(180, 170, 221, 71))
        self.certiDoctor.setObjectName("certiDoctor")
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(130, 290, 121, 28))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(280, 290, 93, 28))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "Multivalue"))
        self.label_11.setText(_translate("Dialog", "Degree :"))
        self.label_12.setText(_translate("Dialog", "Certification :"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.cancel.setText(_translate("Dialog", "Cancel"))

    def show(self):
        self.Dialog.show()


    def add(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='hospital',
                                                user='root',
                                                password='root')
            objdata = (self.employID,self.name,self.personalID,self.gender,self.birthDate,self.joinDate,self.salary,self.department,self.phones)
                #TODO add doctor data
            sqlQuery = "insert into "+"doctor"+"(Employee_ID) " \
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

        self.ui = EmployeeController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

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
