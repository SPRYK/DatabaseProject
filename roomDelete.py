import RoomController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 168)
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(220, 110, 93, 28))
        self.cancel.setObjectName("cancel")
        self.delete_2 = QtWidgets.QPushButton(self.Dialog)
        self.delete_2.setGeometry(QtCore.QRect(70, 110, 93, 28))
        self.delete_2.setObjectName("delete_2")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(200, 40, 161, 22))
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 151, 20))
        self.label.setObjectName("label")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.delete_2.clicked.connect(self.delete)
        self.cancel.clicked.connect(self.back)         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.label.setText(_translate("Dialog", "Delete by Room ID :"))


    def show(self):
        self.Dialog.show()


    def delete(self):
        roomID = self.id.text()
        #TODO delete room

        
        self.ui = RoomController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
        
        
    def back(self):
        self.ui = RoomController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
