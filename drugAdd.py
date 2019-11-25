import DrugController, mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 215)
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(220, 150, 93, 28))
        self.cancel.setObjectName("cancel")
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(70, 150, 121, 28))
        self.ok.setObjectName("ok")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 70, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(160, 70, 171, 22))
        self.name.setObjectName("name")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(160, 20, 171, 22))
        self.id.setObjectName("id")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.label_5.setText(_translate("Dialog", " Drug Name :"))
        self.label_4.setText(_translate("Dialog", " Drug ID :"))


    def show(self):
        self.Dialog.show()


    def add(self):
        drugID = self.id.text()
        drugName = self.name.text()
        #TODO add new drug to database
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='OC0kkgwRe4x38s')
            objdata = (drugID,drugName)
                
            sqlQuery = "insert into "+"drug"+"(Drug_ID, Drug_Name) " \
                        "values(%s,%s)"
                
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

        
        self.ui = DrugController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
        
    def back(self):
        self.ui = DrugController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show() 
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
