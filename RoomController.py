# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RoomController.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import MainController
import roomAdd,roomAddBed,roomDelete,roomDeleteBed,roomEdit,roomSearch

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 100, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 30, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 100, 141, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 250, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 170, 141, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 170, 141, 28))
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add_room)
        self.pushButton_2.clicked.connect(self.edit_room)
        self.pushButton_3.clicked.connect(self.delete_room)
        self.pushButton_4.clicked.connect(self.search_room)
        self.pushButton_5.clicked.connect(self.delete_bed)
        self.pushButton_6.clicked.connect(self.back)
        self.pushButton_7.clicked.connect(self.add_bed)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Edit Room"))
        self.pushButton_3.setText(_translate("Dialog", "Delete Room"))
        self.pushButton_4.setText(_translate("Dialog", "Search Room"))
        self.pushButton_6.setText(_translate("Dialog", "Back"))
        self.pushButton.setText(_translate("Dialog", "Add New Room"))
        self.pushButton_5.setText(_translate("Dialog", "Delete Bed"))
        self.pushButton_7.setText(_translate("Dialog", "Add Bed"))

    def show(self):
        self.Dialog.show()

    def back(self):
        self.ui = MainController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def add_room(self):
        self.ui = roomAdd.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def edit_room(self):
        self.ui = roomEdit.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def delete_room(self):
        self.ui = roomDelete.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def search_room(self):
        self.ui = roomSearch.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def delete_bed(self):
        self.ui = roomDelete.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def add_bed(self):
        self.ui = roomAddBed.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
