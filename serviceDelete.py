import ServiceController
from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
password = 'root'


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(463, 300)
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 131, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 20))
        self.label.setObjectName("label")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.cancel.setObjectName("cancel")
        self.delete_2 = QtWidgets.QPushButton(self.Dialog)
        self.delete_2.setGeometry(QtCore.QRect(140, 210, 93, 28))
        self.delete_2.setObjectName("delete_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(200, 100, 171, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(180, 30, 161, 22))
        self.id.setObjectName("id")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(20, 70, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(350, 30, 93, 28))
        self.fillButton.setObjectName("fillButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)


        self.delete_2.clicked.connect(self.delete)
        self.cancel.clicked.connect(self.back)
        self.fillButton.clicked.connect(self.fill)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Selected Service :"))
        self.label.setText(_translate("Dialog", "Delete by Service ID :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.fillButton.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()


    def delete(self):
        serviceID = self.id.text()
        #TODO delete service
        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('delete from {} where {} = \'{}\''.format('service', 'Service_ID', serviceID))
            print('executed')
            connection.commit()
            #result = cursor.fetchall()
            #print(result)
            connection.close()
        except Exception as e :
            print(e)


        self.ui = ServiceController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()        

    def fill(self):
        serviceID = self.id.text()
        #TODO fill data
        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('select * from {} where ({} = \'{}\')'.format('service', 'Service_ID', serviceID))
            print('executed')
            #connection.commit()
            result = cursor.fetchall()
            print(result)
            connection.close()
            self.textBrowser.clear()
            if len(result) > 0 :
                self.textBrowser.append(str(result[0][1:4]))
        except Exception as e :
            print(e)
        return None
        #example
        self.textBrowser.append("service1")
        
        

    def back(self):
        self.ui = ServiceController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()            

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
