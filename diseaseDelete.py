import DiseaseController
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(464, 481)
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(260, 410, 93, 28))
        self.cancel.setObjectName("cancel")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(190, 30, 161, 22))
        self.id.setObjectName("id")
        self.delete_2 = QtWidgets.QPushButton(self.Dialog)
        self.delete_2.setGeometry(QtCore.QRect(110, 410, 93, 28))
        self.delete_2.setObjectName("delete_2")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 141, 20))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(190, 100, 241, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(50, 70, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fill = QtWidgets.QPushButton(self.Dialog)
        self.fill.setGeometry(QtCore.QRect(360, 30, 93, 28))
        self.fill.setObjectName("fill")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.delete_2.clicked.connect(self.delete)
        self.cancel.clicked.connect(self.back)        
        self.fill.clicked.connect(self.filling)

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.label_2.setText(_translate("Dialog", "Selected Disease :"))
        self.label.setText(_translate("Dialog", "Delete by Disease ID :"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.fill.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()


    def delete(self):
        diseaseID = self.id.text()
        #TODO add disease to self.textBrowser then delete?? not sure haha
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (diseaseID,)
            sqlQuery = "select * from "+"disease"+" where Disease_ID = %s"
            cursor_s = connection.cursor()
            cursor_s.execute(sqlQuery, objdata)
            records = cursor_s.fetchone()
                    
        except Exception as e:
            retmsg = ["1", "Error"]
            print(e)
            print("Erorr 1")
        else :
            retmsg = ["1", "Not Found"]
            try:
                if records[0] != "" :
                    try:
                        sqlQuery = "delete from "+"disease"+" where Disease_ID = %s"    
                        cursor_s.execute(sqlQuery, objdata)
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
                    cursor_s.close()
                if(retmsg[0]=='1') :
                    self.textBrowser.append(retmsg[1])
                else :
                    self.textBrowser.append(str(records[1]))
            except Exception as e:
                print(e)
                print("Erorr 4")

        #delete phone
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
        
    def back(self):
        self.ui = DiseaseController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()


    def filling(self):
        diseaseID = self.id.text()
        #TODO fill data
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
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
