# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DrugController.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import MainController
import drugAdd, drugDelete, drugEdit, drugSearch

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.pushButton_4 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 100, 141, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 100, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 250, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 30, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add_drug)
        self.pushButton_2.clicked.connect(self.edit_drug)
        self.pushButton_3.clicked.connect(self.delete_drug)
        self.pushButton_4.clicked.connect(self.search_drug)
        self.pushButton_6.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_4.setText(_translate("Dialog", "Search Drug"))
        self.pushButton_2.setText(_translate("Dialog", "Edit Drug"))
        self.pushButton.setText(_translate("Dialog", "Add New Drug"))
        self.pushButton_6.setText(_translate("Dialog", "Back"))
        self.pushButton_3.setText(_translate("Dialog", "Delete Drug"))


    def show(self):
        self.Dialog.show()

    def back(self):
        self.ui = MainController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def add_drug(self):
        self.ui = drugAdd.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def edit_drug(self):
        self.ui = drugEdit.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def delete_drug(self):
        self.ui = drugDelete.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def search_drug(self):
        self.ui = drugSearch.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
