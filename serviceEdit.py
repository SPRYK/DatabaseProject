import ServiceController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(459, 320)
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 120, 121, 20))
        self.label_5.setObjectName("label_5")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(200, 120, 171, 22))
        self.name.setObjectName("name")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(150, 30, 161, 22))
        self.id.setObjectName("id")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(270, 240, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(100, 180, 101, 20))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 161, 20))
        self.label.setObjectName("label")
        self.type = QtWidgets.QComboBox(self.Dialog)
        self.type.setGeometry(QtCore.QRect(210, 180, 151, 22))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.edit = QtWidgets.QPushButton(self.Dialog)
        self.edit.setGeometry(QtCore.QRect(120, 240, 93, 28))
        self.edit.setObjectName("edit")
        self.fillButton = QtWidgets.QPushButton(self.Dialog)
        self.fillButton.setGeometry(QtCore.QRect(330, 30, 93, 28))
        self.fillButton.setObjectName("fillButton")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(30, 70, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.edit.clicked.connect(self.editing)
        self.cancel.clicked.connect(self.back)
        self.fillButton.clicked.connect(self.fill)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Service Name :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_7.setText(_translate("Dialog", "Service Type :"))
        self.label.setText(_translate("Dialog", "Edit by Service ID :"))
        self.type.setItemText(0, _translate("Dialog", "Medical care"))
        self.type.setItemText(1, _translate("Dialog", "Surgical"))
        self.type.setItemText(2, _translate("Dialog", "Diagnostic"))
        self.type.setItemText(3, _translate("Dialog", "Blood"))
        self.edit.setText(_translate("Dialog", "Edit"))
        self.fillButton.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()

    def editing(self):
        serviceID = self.id.text()
        serviceName = self.name.text()
        serviceType = str(self.type.currentText())
        #TODO edit service


        self.ui = ServiceController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()          
 
    def back(self):
        self.ui = ServiceController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()         

    def fill(self):
        serviceID = self.id.text()
        #TODO fill data

        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
