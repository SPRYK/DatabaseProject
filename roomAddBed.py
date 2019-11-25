import RoomController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.roomList = QtWidgets.QComboBox(self.Dialog)
        self.roomList.setGeometry(QtCore.QRect(180, 100, 151, 22))
        self.roomList.setObjectName("roomList")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 40, 101, 20))
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(170, 40, 171, 22))
        self.id.setObjectName("id")
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(80, 200, 121, 28))
        self.ok.setObjectName("ok")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 100, 101, 20))
        self.label_7.setObjectName("label_7")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(230, 200, 93, 28))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)


        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)


    def add(self):
        bedID = self.id.text()
        patientRoom = str(self.roomList.currentText())
        #TODO add bed to database



        self.ui = RoomController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def back(self):
        self.ui = RoomController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()          
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", " Bed ID :"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.label_7.setText(_translate("Dialog", "Choose Room :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))


    def show(self):
        self.Dialog.show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
