from PyQt5 import QtCore, QtGui, QtWidgets
import MainController
import employeeAdd, employeeDelete, employeeEdit, employeeSearch

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 20, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 20, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 90, 141, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 90, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 240, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add_employee)
        self.pushButton_2.clicked.connect(self.edit_employee)
        self.pushButton_3.clicked.connect(self.delete_employee)
        self.pushButton_4.clicked.connect(self.search_employee)
        self.pushButton_6.clicked.connect(self.back)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Add New Employee"))
        self.pushButton_3.setText(_translate("Dialog", "Delete Employee"))
        self.pushButton_4.setText(_translate("Dialog", "Search Employee"))
        self.pushButton_2.setText(_translate("Dialog", "Edit Employee"))
        self.pushButton_6.setText(_translate("Dialog", "Back"))

    def show(self):
        self.Dialog.show()

    def back(self):
        self.ui = MainController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def add_employee(self):
        self.ui = employeeAdd.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        
    def edit_employee(self):
        self.ui = employeeEdit.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def delete_employee(self):
        self.ui = employeeDelete.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def search_employee(self):
        self.ui = employeeSearch.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
