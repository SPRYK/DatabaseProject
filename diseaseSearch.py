import DiseaseController
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(461, 409)
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(240, 360, 93, 28))
        self.cancel.setObjectName("cancel")
        self.search = QtWidgets.QPushButton(self.Dialog)
        self.search.setGeometry(QtCore.QRect(90, 360, 93, 28))
        self.search.setObjectName("search")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(194, 30, 161, 22))
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(54, 130, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(44, 30, 151, 20))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(180, 120, 241, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(40, 70, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.search.clicked.connect(self.searching)
        self.cancel.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.search.setText(_translate("Dialog", "Search"))
        self.label_2.setText(_translate("Dialog", "Selected Disease :"))
        self.label.setText(_translate("Dialog", "Search by Disease ID :"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


    def show(self):
        self.Dialog.show()


    def searching(self):
        diseaseID = self.id.text()
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (diseaseID,)
            sqlQuery = "select * from "+"disease"+" where Disease_ID = %s"

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
                        self.textBrowser.append("ID = "+str(row[0])+"\nName = "+str(row[1])+"\nSpecialty :")

                        #special fetcher
                        try:
                            connection_s = mysql.connector.connect(host='localhost',database='hospital',user='root',password='root')
                            sqlQuery_s = "select * from "+"disease_specialty"+" where Disease_ID = %s"
                            objdata_s = (str(row[0]),)

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
                                self.textBrowser.append("          "+retmsg_s[1])
                            else :
                                for spec in specs:
                                    self.textBrowser.append("          "+str(spec[1]))        
            except Exception as e:
                print(e)
                print("Erorr 4")  
        
        #example

        
        
    def back(self):
        self.ui = DiseaseController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()            
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
