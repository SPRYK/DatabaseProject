from PyQt5 import QtCore, QtGui, QtWidgets
import DrugController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 364)
        self.textEdit = QtWidgets.QTextEdit(self.Dialog)
        self.textEdit.setGeometry(QtCore.QRect(170, 140, 161, 87))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 270, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 140, 131, 20))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 270, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 70, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 70, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 20, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_6.setText(_translate("Dialog", " Drug Description :"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.label_5.setText(_translate("Dialog", " Drug Name :"))
        self.label_4.setText(_translate("Dialog", " Drug ID :"))


    def show(self):
        self.Dialog.show()

    def add(self):
        drugDesc = self.textEdit.toPlainText()
        drugID = self.lineEdit_2.text()
        drugName = self.lineEdit_3.text()
        #TODO add new drug to database
        

    def back(self):
        self.ui = DrugController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()  

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
