import sys, mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(486, 543)
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(220, 20, 161, 22))
        self.id.setObjectName("id")
        self.search = QtWidgets.QPushButton(self.Dialog)
        self.search.setGeometry(QtCore.QRect(100, 480, 93, 28))
        self.search.setObjectName("search")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 201, 20))
        self.label.setObjectName("label")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(250, 480, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 141, 20))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(40, 110, 391, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(200, 160, 241, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 60, 61, 20))
        self.label_3.setObjectName("label_3")
        self.degree = QtWidgets.QLineEdit(self.Dialog)
        self.degree.setGeometry(QtCore.QRect(220, 60, 161, 22))
        self.degree.setObjectName("degree")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.search.clicked.connect(self.query)
        self.cancel.clicked.connect(self.exit)         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Search by Patient Blood group :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Selected employee :"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Disease ID :"))


    def show(self):
        self.Dialog.show()

    def exit(self):
        sys.exit()

        
    def query(self):
        blood = self.id.text()
        disease = self.degree.text()
        buff1 = []
        buff2 = []
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (disease,)
            sqlQuery = "select * from "+"diagnose"+" where Disease_ID = %s"

            cursor = connection.cursor(buffered=True)
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchall()
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
        finally:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                if(retmsg[0]=='1') :
                    self.textBrowser.append(retmsg[1])

        for row in records:
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='hospital',
                                                    user='root',
                                                    password='root')
                objdata = (row[0],)
                sqlQuery = "select * from "+"trearment"+" where Treatment_ID = %s"
                cursor = connection.cursor(buffered=True)
                cursor.execute(sqlQuery, objdata)
                buff1 += cursor.fetchall()
                
            except:
                retmsg = ["1", "Error"]
            else :
                retmsg = ["1", "Not Found"]
            finally:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                if(retmsg[0]=='1') :
                    self.textBrowser.append(retmsg[1])
        for row in buff1:
            try:
                connection = mysql.connector.connect(host='localhost',
                                            database='hospital',
                                            user='root',
                                            password='root')
                objdata = (row[3],)
                sqlQuery = "select * from "+"patient"+" where Patient_ID = %s"

                cursor = connection.cursor(buffered=True)
                cursor.execute(sqlQuery, objdata)
                buff2 += cursor.fetchall()
                            
            except:
                retmsg = ["1", "Error"]

        for i in buff2:
            if i[5] == blood:
                self.textBrowser.append(i)
                                    
                                    
                                            


                                            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
