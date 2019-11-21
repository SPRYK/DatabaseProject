from PyQt5 import QtCore, QtGui, QtWidgets
import RoomController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(180, 100, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 40, 101, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 40, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 200, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 100, 151, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 200, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)           

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", " Bed ID :"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.label_7.setText(_translate("Dialog", "Choose Patient Room :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))


    def show(self):
        self.Dialog.show()

    def add(self):
        bedID = self.lineEdit_2.text()
        patientRoom = str(self.comboBox.currentText())
        #TODO add bed to database
        
        

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
