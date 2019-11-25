import EmployeeController, mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(472, 496)
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(270, 400, 93, 28))
        self.cancel.setObjectName("cancel")
        self.eid = QtWidgets.QLineEdit(self.Dialog)
        self.eid.setGeometry(QtCore.QRect(190, 40, 161, 22))
        self.eid.setObjectName("eid")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(44, 120, 131, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 141, 20))
        self.label.setObjectName("label")
        self.delete_2 = QtWidgets.QPushButton(self.Dialog)
        self.delete_2.setGeometry(QtCore.QRect(120, 400, 93, 28))
        self.delete_2.setObjectName("delete_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(190, 110, 241, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(20, 80, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fill = QtWidgets.QPushButton(self.Dialog)
        self.fill.setGeometry(QtCore.QRect(360, 40, 93, 28))
        self.fill.setObjectName("fill")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.delete_2.clicked.connect(self.delete)
        self.cancel.clicked.connect(self.back)
        self.fill.clicked.connect(self.fill)  

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Selected Employee :"))
        self.label.setText(_translate("Dialog", "Delete by Employee ID :"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.fill.setText(_translate("Dialog", "Fill"))


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
            print("Erorr 1")
        else :
            retmsg = ["1", "Not Found"]
        finally:
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                if(retmsg[0]=='1') :
                    self.textBrowser.append(retmsg[1])
                else :
                    self.textBrowser.append(str(records[2]))
            except Exception as e:
                print(e)
                print("Erorr 4")


    def delete(self):
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
            print("Erorr 1")
        else :
            retmsg = ["1", "Not Found"]
            try:
                if records[0] != "" :
                    try:
                        sqlQuery = "delete from "+'employee'+" where Employee_ID = %s"  
                        if (employeeID=='') :
                            sqlQuery = "delete from "+'employee'+" where Employee_Name = %s"    
                        cursor = connection.cursor()
                        cursor.execute(sqlQuery, objdata)
                        connection.commit()
                        retmsg = ["0", "Found"]
                    except Exception as e:
                        retmsg = ["1", "Multiple Data"]
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
                if(retmsg[0]=='1') :
                    self.textBrowser.append(retmsg[1])
                else :
                    self.textBrowser.append(str(records[2]))
            except Exception as e:
                print(e)
                print("Erorr 4")
                

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
