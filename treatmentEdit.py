# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treatmentEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 372)
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(170, 80, 51, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(80, 250, 101, 20))
        self.label_11.setObjectName("label_11")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(190, 250, 141, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(240, 80, 81, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 160, 141, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 120, 91, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 160, 121, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(110, 200, 71, 20))
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 200, 141, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 310, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 80, 111, 20))
        self.label_6.setObjectName("label_6")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(330, 80, 81, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 310, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 120, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 131, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 20, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton_3.setText(_translate("Dialog", "High"))
        self.label_11.setText(_translate("Dialog", "Appointment ID :"))
        self.radioButton_4.setText(_translate("Dialog", "Medium"))
        self.label_8.setText(_translate("Dialog", "Assign Doctor :"))
        self.label_9.setText(_translate("Dialog", "Diagnose Disease :"))
        self.label_10.setText(_translate("Dialog", "Use Drug :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_6.setText(_translate("Dialog", "Emergency Level :"))
        self.radioButton_5.setText(_translate("Dialog", "Low"))
        self.pushButton.setText(_translate("Dialog", "Edit"))
        self.label_4.setText(_translate("Dialog", "Edit by Treatment ID :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
