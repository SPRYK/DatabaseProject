import RoomController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 133)
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(80, 80, 121, 28))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(230, 80, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 101, 20))
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(170, 20, 171, 22))
        self.id.setObjectName("id")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", " Room ID :"))


    def show(self):
        self.Dialog.show()


    def add(self):
        roomID = self.id.text()
        #TODO add room to database
        


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
