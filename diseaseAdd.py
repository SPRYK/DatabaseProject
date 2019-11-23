from PyQt5 import QtCore, QtGui, QtWidgets
import DiseaseController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(422, 361)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 20, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 70, 101, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 70, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 300, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 130, 101, 20))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 130, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 131, 20))
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.Dialog)
        self.textEdit.setGeometry(QtCore.QRect(170, 180, 161, 87))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", " Disease ID :"))
        self.label_5.setText(_translate("Dialog", " Disease Name :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.label_7.setText(_translate("Dialog", "Cure by Drug :"))
        self.label_6.setText(_translate("Dialog", " Disease Description :"))


    def show(self):
        self.Dialog.show()


    def add(self):
        diseaseID = self.lineEdit_2.text()
        diseaseName = self.lineEdit_3.text()
        diseaseDesc = self.textEdit.toPlainText()
        Drug = str(self.comboBox.currentText())
        #TODO add disease to database


        
        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()

        
    def back(self):
        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
