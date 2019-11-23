from PyQt5 import QtCore, QtGui, QtWidgets
import ServiceController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 190, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 30, 101, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 30, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 120, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 120, 101, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 190, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 70, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 70, 121, 20))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.label_4.setText(_translate("Dialog", " Service ID :"))
        self.label_7.setText(_translate("Dialog", "Service Type :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_5.setText(_translate("Dialog", " Service Name :"))


    def show(self):
        self.Dialog.show()

    def add(self):
        serviceID = self.lineEdit_2.text()
        serviceName = self.lineEdit_3.text()
        serviceType = str(self.comboBox.currentText())
        #TODO add new Service to database




        self.ui = ServiceController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        
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
