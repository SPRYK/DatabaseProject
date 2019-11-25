import patientController
from PyQt5 import QtCore, QtGui, QtWidgets

import datetime

import mysql.connector
password = 'root'


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(497, 566)
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 141, 20))
        self.label_2.setObjectName("label_2")
        self.delete_2 = QtWidgets.QPushButton(self.Dialog)
        self.delete_2.setGeometry(QtCore.QRect(100, 500, 93, 28))
        self.delete_2.setObjectName("delete_2")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(250, 500, 93, 28))
        self.cancel.setObjectName("cancel")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(156, 110, 311, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 101, 20))
        self.label_3.setObjectName("label_3")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(130, 40, 171, 22))
        self.id.setObjectName("id")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(330, 40, 93, 28))
        self.fillButton.setObjectName("fillButton")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(20, 80, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.delete_2.clicked.connect(self.delete)
        self.fillButton.clicked.connect(self.fill)
        self.cancel.clicked.connect(self.back)        

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Selected Treatment :"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Treatment ID :"))
        self.fillButton.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()

    def delete(self):
        treatmentID = self.id.text()
        #TODO add treatment to self.textBrower then delete??? not sure haha
        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('delete from {} where {} = \'{}\''.format('treatment', 'Treatment_ID', treatmentID))
            print('executed')
            connection.commit()
            #result = cursor.fetchall()
            #print(result)
            connection.close()
        except Exception as e :
            print(e)

        #example
        #self.textBrowser.append('treatment1')

    def fill(self):
        treatmentID = self.id.text()
        #TODO fill data
        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('select * from {} where ({} = \'{}\')'.format('treatment', 'Treatment_ID', treatmentID))
            print('executed')
            #connection.commit()
            result = cursor.fetchall()
            print(result)
            self.textBrowser.clear()
            if len(result) > 0 :
                patientID = result[0][3]
                cursor.execute('select * from patient where Patient_ID = \'{}\''.format(patientID))
                patientName = cursor.fetchall()[0][2]
                self.textBrowser.append('{} {} {}'.format(patientName, str(result[0][1]), result[0][2]))
            connection.close()
        except Exception as e :
            print(e)
        
        
    def back(self):
        self.ui = patientController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
