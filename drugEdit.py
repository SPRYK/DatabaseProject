import DrugController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(444, 260)
        self.edit = QtWidgets.QPushButton(self.Dialog)
        self.edit.setGeometry(QtCore.QRect(90, 200, 121, 28))
        self.edit.setObjectName("edit")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(180, 130, 171, 22))
        self.name.setObjectName("name")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 130, 81, 20))
        self.label_5.setObjectName("label_5")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(240, 200, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 141, 20))
        self.label.setObjectName("label")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(150, 50, 161, 22))
        self.id.setObjectName("id")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 90, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(330, 50, 93, 28))
        self.fillButton.setObjectName("fillButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.edit.clicked.connect(self.editing)
        self.cancel.clicked.connect(self.back)
        self.fillButton.clicked.connect(self.fill)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.edit.setText(_translate("Dialog", "Edit"))
        self.label_5.setText(_translate("Dialog", " Drug Name :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Edit by Drug ID :"))
        self.fillButton.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()


    def editing(self):
        drugID = self.id.text()
        drugName = self.name.text()
        #TODO edit drug



        self.ui = DrugController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()        

    def back(self):
        self.ui = DrugController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def fill(self):
        drugID = self.id.text()
        #TODO fill data
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
