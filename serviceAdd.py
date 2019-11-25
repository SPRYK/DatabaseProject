import ServiceController
from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
password = 'root'

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(80, 240, 121, 28))
        self.ok.setObjectName("ok")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 30, 101, 20))
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(180, 30, 171, 22))
        self.id.setObjectName("id")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 120, 101, 20))
        self.label_7.setObjectName("label_7")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(230, 240, 93, 28))
        self.cancel.setObjectName("cancel")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(180, 70, 171, 22))
        self.name.setObjectName("name")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 70, 121, 20))
        self.label_5.setObjectName("label_5")
        self.type = QtWidgets.QComboBox(self.Dialog)
        self.type.setGeometry(QtCore.QRect(180, 120, 151, 22))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.departmentList = QtWidgets.QComboBox(self.Dialog)
        self.departmentList.setGeometry(QtCore.QRect(180, 170, 151, 22))
        self.departmentList.setObjectName("departmentList")
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 170, 151, 20))
        self.label_8.setObjectName("label_8")        

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)

        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('select * from department')
            print('executed')
            #connection.commit()
            result = cursor.fetchall()
            print(result)
            connection.close()
            for e in result :
                self.departmentList.addItem(e[1])
        except Exception as e :
            print(e)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.label_4.setText(_translate("Dialog", " Service ID :"))
        self.label_7.setText(_translate("Dialog", "Service Type :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_5.setText(_translate("Dialog", " Service Name :"))
        self.type.setItemText(0, _translate("Dialog", "Medical care"))
        self.type.setItemText(1, _translate("Dialog", "Surgical"))
        self.type.setItemText(2, _translate("Dialog", "Diagnostic"))
        self.type.setItemText(3, _translate("Dialog", "Blood"))
        self.label_8.setText(_translate("Dialog", "Selected Department :"))        


    def show(self):
        self.Dialog.show()


    def add(self):
        serviceID = self.id.text()
        serviceName = self.name.text()
        serviceType = str(self.type.currentText())
        deptName = self.departmentList.currentText()
        #TODO add new Service to database
        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            print('select * from department where Dept_Name = \'{}\''.format(deptName))
            cursor.execute('select * from department where Dept_Name = \'{}\''.format(deptName))
            result = cursor.fetchall()
            if len(result) == 0 : return None
            deptID = result[0][0]
            into = 'Service_ID, Service_Name, Service_Type, Dept_ID'
            value = '\'{}\', \'{}\', \'{}\', \'{}\''.format(serviceID, serviceName, serviceType, deptID)
            print('insert into {} ({}) value ({})'.format('service', into, value))
            cursor.execute('insert into {} ({}) value ({})'.format('service', into, value))
            print('executed')
            connection.commit()
            #result = cursor.fetchall()
            #print(result)
            connection.close()
        except Exception as e :
            print(e)



        self.ui = ServiceController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        
    def back(self):
        self.ui = ServiceController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()         

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
