from PyQt5 import QtCore, QtGui, QtWidgets
import patientController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(457, 369)
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 30, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 121, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 41, 20))
        self.label_2.setObjectName("label_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 180, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 130, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton = QtWidgets.QRadioButton(self.Dialog)
        self.radioButton.setGeometry(QtCore.QRect(180, 180, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 130, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 180, 51, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 90, 171, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 320, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 320, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(350, 220, 55, 16))
        self.label_7.setObjectName("label_7")
        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        #self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.back)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Edit by Patient ID :"))
        self.label_2.setText(_translate("Dialog", "Name :"))
        self.radioButton_2.setText(_translate("Dialog", "Female"))
        self.radioButton.setText(_translate("Dialog", "Male"))
        self.label_3.setText(_translate("Dialog", "Personal ID :"))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        self.pushButton.setText(_translate("Dialog", "Edit"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_7.setText(_translate("Dialog", "ยังไงดี"))

    def show(self):
        self.Dialog.show()

    def back(self):
        self.ui = patientController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    #TODO edit?? how??
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
