from PyQt5 import QtCore, QtGui, QtWidgets
import ServiceController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 90, 121, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 90, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(100, 150, 101, 20))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 161, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(210, 150, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.back)         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Service Name :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_7.setText(_translate("Dialog", "Service Type :"))
        self.label.setText(_translate("Dialog", "Edit by Service ID :"))
        self.pushButton.setText(_translate("Dialog", "Edit"))


    def show(self):
        self.Dialog.show()

    def edit(self):
        serviceID = self.lineEdit.text()
        serviceName = self.lineEdit_3.text()
        serviceType = str(self.comboBox.currentText())
        #TODO edit serviceName and serviceType by serviceID

        
 
    def back(self):
        self.ui = ServiceController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()        
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
