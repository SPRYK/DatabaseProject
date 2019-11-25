import DiseaseController
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(456, 361)
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(170, 20, 161, 22))
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(150, 100, 171, 22))
        self.name.setObjectName("name")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 100, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 131, 20))
        self.label_6.setObjectName("label_6")
        self.specialty = QtWidgets.QLineEdit(self.Dialog)
        self.specialty.setGeometry(QtCore.QRect(150, 150, 161, 87))
        self.specialty.setObjectName("specialty")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(240, 290, 93, 28))
        self.cancel.setObjectName("cancel")
        self.edit = QtWidgets.QPushButton(self.Dialog)
        self.edit.setGeometry(QtCore.QRect(90, 290, 121, 28))
        self.edit.setObjectName("edit")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 60, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(350, 20, 93, 28))
        self.fillButton.setObjectName("fillButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.edit.clicked.connect(self.editing)
        self.cancel.clicked.connect(self.back)
        self.fillButton.clicked.connect(self.fill)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Edit by Disease ID :"))
        self.label_5.setText(_translate("Dialog", " Disease Name :"))
        self.label_6.setText(_translate("Dialog", "Disease Specialty :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.edit.setText(_translate("Dialog", "Edit"))
        self.fillButton.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()


    def editing(self):
        diseaseID = self.id.text()
        diseaseName = self.name.text()
        diseaseDesc = self.specialty.text()
        #TODO edit disease
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (diseaseID,)
            sqlQuery = "select * from "+"disease"+" where Disease_ID = %s"
            
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
                        sqlQuery = "update disease set Disease_Name = %s"
                        objdata = (diseaseName,)
                        
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

        #delete spec
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (diseaseID,)
            sqlQuery = "delete from "+"disease_specialty"+" where Disease_ID = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
        except Exception as e:
            retmsg_s = ["1", "writing error"]
            print(e)
            print("Delete Error")
        finally:
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
            except Exception as e:
                print(e)
                print("Erorr 4")

        #add disease_specialty
        try:
            connection = mysql.connector.connect(host='localhost',database='hospital',user='root',password='root')
            sqlQuery = "insert into "+"disease_specialty"+"(Disease_ID, Specialty) "+"values(%s,%s)"

            for desc in diseaseDesc.split():
                objdata = (diseaseID,desc)
                cursor = connection.cursor()
                cursor.execute(sqlQuery, objdata)
                connection.commit()
            
        except Exception as e:
            retmsg_s = ["1", "writing error"]
            print(e)
            print("Fetch Error")
        else :
            retmsg_s = ["0", "writing done"]
        finally :
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
            except Exception as e:
                print(e)


        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def back(self):
        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()


    def fill(self):
        diseaseID = self.id.text()
        #TODO fill data
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (diseaseID,)
            sqlQuery = "select * from "+"disease"+" where Disease_ID = %s"

            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
                    
        except Exception as e:
            retmsg = ["1", "Error"]
            print(e)
        else :
            retmsg = ["1", "Not Found"]
            try:
                if records[0] != "" :
                    retmsg = ["0", "Found"]
            except Exception as e:
                print(e)
                print("Erorr 2")
        finally:
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                if(retmsg[0]=='0') :
                    self.name.setText(str(records[1]))
                    try:
                        connection_s = mysql.connector.connect(host='localhost',database='hospital',user='root',password='root')
                        sqlQuery_s = "select * from "+"disease_specialty"+" where Disease_ID = %s"
                        objdata_s = (diseaseID,)

                        cursor_s = connection_s.cursor(buffered=True)
                        cursor_s.execute(sqlQuery_s, objdata_s)
                        specs = cursor_s.fetchall()
                    except Exception as e:
                        retmsg_s = ["1","Error"]
                        print(e)
                        print("Fetch Error")
                    else :
                        retmsg_s = ["1", "Not Found"]
                        try:
                            if specs[0] != "" :
                                retmsg_s = ["0", "Found"]
                        except Exception as e:
                            print(e)
                            print("Erorr 2_s")
                    finally :
                        if (connection_s.is_connected()):
                            connection_s.close()
                            cursor_s.close()

                        if(retmsg_s[0]=='1') :
                            self.specialty.setText(retmsg_s[1])
                        else :
                            temp_text = ""
                            index = 0
                            for spec in specs:
                                if(index == 0) :
                                    temp_text = str(spec[1])
                                    index = 1
                                else:
                                    temp_text = temp_text+" "+str(spec[1])
                            self.specialty.setText(temp_text)
            except Exception as e:
                print(e)
                print("Erorr 4")

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
