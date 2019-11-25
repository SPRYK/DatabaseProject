import DiseaseController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(456, 361)
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(170, 20, 161, 22))
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(150, 100, 171, 22))
        self.name.setObjectName("name")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 100, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 131, 20))
        self.label_6.setObjectName("label_6")
        self.specialty = QtWidgets.QPlainTextEdit(self.Dialog)
        self.specialty.setGeometry(QtCore.QRect(150, 150, 161, 87))
        self.specialty.setObjectName("specialty")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(240, 290, 93, 28))
        self.cancel.setObjectName("cancel")
        self.edit = QtWidgets.QPushButton(self.Dialog)
        self.edit.setGeometry(QtCore.QRect(90, 290, 121, 28))
        self.edit.setObjectName("edit")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 60, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(350, 20, 93, 28))
        self.fillButton.setObjectName("fillButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.edit.clicked.connect(self.editing)
        self.cancel.clicked.connect(self.back)
        self.fillButton.clicked.connect(self.fill)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Edit by Disease ID :"))
        self.label_5.setText(_translate("Dialog", " Disease Name :"))
        self.label_6.setText(_translate("Dialog", "Disease Specialty :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.edit.setText(_translate("Dialog", "Edit"))
        self.fillButton.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()


    def editing(self):
        diseaseID = self.id.text()
        diseaseName = self.name.text()
        diseaseDesc = self.specialty.toPlainText()
        #TODO edit disease


        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()

    def back(self):
        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()


    def fill(self):
        diseaseID = self.id.text()
        #TODO fill data


        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
