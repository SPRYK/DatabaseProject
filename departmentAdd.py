import DepartmentController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 204)
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 101, 20))
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(160, 20, 171, 22))
        self.id.setObjectName("id")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 121, 20))
        self.label_5.setObjectName("label_5")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(160, 70, 171, 22))
        self.name.setObjectName("name")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(230, 140, 93, 28))
        self.cancel.setObjectName("cancel")
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(80, 140, 121, 28))
        self.ok.setObjectName("ok")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", " Department ID :"))
        self.label_5.setText(_translate("Dialog", "Department Name :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.ok.setText(_translate("Dialog", "Ok"))


    def show(self):
        self.Dialog.show()


    def add(self):
        departID = self.id.text()
        departName = self.name.text()
        #TODO add new department to database



        self.ui = DepartmentController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()
        
    def back(self):
        self.ui = DepartmentController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
