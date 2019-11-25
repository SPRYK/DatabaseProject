import DepartmentController
from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
password = 'root'


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(474, 232)
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(190, 30, 161, 22))
        self.id.setObjectName("id")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(250, 160, 93, 28))
        self.cancel.setObjectName("cancel")
        self.edit = QtWidgets.QPushButton(self.Dialog)
        self.edit.setGeometry(QtCore.QRect(100, 160, 93, 28))
        self.edit.setObjectName("edit")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 161, 20))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 90, 121, 20))
        self.label_5.setObjectName("label_5")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(180, 90, 171, 22))
        self.name.setObjectName("name")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 60, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(370, 30, 93, 28))
        self.fillButton.setObjectName("fillButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.edit.clicked.connect(self.editing)
        self.cancel.clicked.connect(self.back)
        self.fillButton.clicked.connect(self.fill)  

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.edit.setText(_translate("Dialog", "Edit"))
        self.label.setText(_translate("Dialog", "Edit by Department ID :"))
        self.label_5.setText(_translate("Dialog", "Department Name :"))
        self.fillButton.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()

    def back(self):
        self.ui = DepartmentController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()

    def editing(self):
        departID = self.id.text()
        departName = self.name.text()
        #TODO edit by department by departID
        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('update {} set {} = \'{}\' where {} = \'{}\''.format('department', 'Dept_Name', departName, 'Dept_ID', departID))
            print('executed')
            connection.commit()
            #result = cursor.fetchall()
            #print(result)
            connection.close()
        except Exception as e :
            print(e)

        self.ui = DepartmentController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()        

    def fill(self):
        departID = self.id.text()
        #TODO fill data
        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('select * from {} where ({} = \'{}\')'.format('department', 'Dept_ID', departID))
            print('executed')
            #connection.commit()
            result = cursor.fetchall()
            print(result)
            connection.close()
            if len(result) > 0 :
                self.name.setText(result[0][1])
        except Exception as e :
            print(e)

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
