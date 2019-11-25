import EmployeeController, mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(427, 485)
        self.eid = QtWidgets.QLineEdit(self.Dialog)
        self.eid.setGeometry(QtCore.QRect(180, 30, 161, 22))
        self.eid.setObjectName("eid")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 121, 20))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(166, 120, 241, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.search = QtWidgets.QPushButton(self.Dialog)
        self.search.setGeometry(QtCore.QRect(100, 410, 93, 28))
        self.search.setObjectName("search")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 151, 20))
        self.label.setObjectName("label")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(250, 410, 93, 28))
        self.cancel.setObjectName("cancel")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(40, 70, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.search.clicked.connect(self.search)
        self.cancel.clicked.connect(self.back)         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Selected Employee :"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.search.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Search by Employee ID :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))


    def show(self):
        self.Dialog.show()


    def search(self):
        employeeID = self.eid.text()
        
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (employeeID,)
            sqlQuery = "select * from "+"employee"+" where Employee_ID = %s"

            cursor = connection.cursor(buffered=True)
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchall()
                    
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
                if(retmsg[0]=='1') :
                    self.textBrowser.append(retmsg[1])
                else :
                    self.textBrowser.clear()
                    for row in records:
                        self.textBrowser.append("ID ="+str(row[0])+"\nNID ="+str(row[1])+"\nName ="+str(row[2])+"\nGender ="+str(row[3]))
            except Exception as e:
                print(e)
                print("Erorr 4")  
        
        #example

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
