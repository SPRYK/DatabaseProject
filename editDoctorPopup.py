import EmployeeController, mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error

password = ""

class Ui_Dialog(object):
    def __init__(self, employID):
    #def __init__(self):
        self.employID = employID    
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(476, 335)
        self.label_11 = QtWidgets.QLabel(self.Dialog)
        self.label_11.setGeometry(QtCore.QRect(100, 70, 61, 20))
        self.label_11.setObjectName("label_11")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(67, 30, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.degreeDoctor = QtWidgets.QLineEdit(self.Dialog)
        self.degreeDoctor.setGeometry(QtCore.QRect(160, 70, 221, 61))
        self.degreeDoctor.setObjectName("degreeDoctor")
        self.label_12 = QtWidgets.QLabel(self.Dialog)
        self.label_12.setGeometry(QtCore.QRect(70, 160, 91, 20))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.Dialog)
        self.label_10.setGeometry(QtCore.QRect(204, 20, 61, 20))
        self.label_10.setObjectName("label_10")
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(110, 280, 121, 28))
        self.ok.setObjectName("ok")
        self.certiDoctor = QtWidgets.QLineEdit(self.Dialog)
        self.certiDoctor.setGeometry(QtCore.QRect(160, 160, 221, 71))
        self.certiDoctor.setObjectName("certiDoctor")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(270, 280, 93, 28))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.edit)
        self.cancel.clicked.connect(self.back)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_11.setText(_translate("Dialog", "Degree :"))
        self.label_12.setText(_translate("Dialog", "Certification :"))
        self.label_10.setText(_translate("Dialog", "Multivalue"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.cancel.setText(_translate("Dialog", "Cancel"))


    def show(self):
        self.Dialog.show()

    def edit(self):
        #TODO edit data
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='hospital',
                                                user='root',
                                                password=password)
            objdata = (self.employID,)
                
            sqlQuery = "insert into "+"doctor"+"(Employee_ID) " \
                        "values(%s)"
                
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
        except Exception as e:
            print(e)
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()

                
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='hospital',
                                                user='root',
                                                password=password)
            objdata = (self.employID,self.certiDoctor.text())
            sqlQuery = "insert into "+"doctor_certification"+"(Employee_ID,Certification) " \
                        "values(%s, %s)"
                
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
        except Exception as e:
            print(e)
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='hospital',
                                                user='root',
                                                password=password)
            objdata = (self.employID,self.degreeDoctor.text())
                
            sqlQuery = "insert into "+"doctor_degree"+"(Employee_ID, Degree) " \
                        "values(%s, %s)"
                
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
        except Exception as e:
            print(e)
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()

                
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='hospital',
                                                user='root',
                                                password=password)

            objdata = (self.certiDoctor.text(), self.employID)
            sqlQuery = "update doctor_certification set Certification = %s where Employee_ID = %s"            
                
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
        except Exception as e:
            print(e)
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='hospital',
                                                user='root',
                                                password=password)
            objdata = (self.degreeDoctor.text(), self.employID)
            sqlQuery = "update doctor_degree set Degree = %s where Employee_ID = %s"    
                
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
        except Exception as e:
            print(e)
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
