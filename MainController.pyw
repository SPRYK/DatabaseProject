from PyQt5 import QtCore, QtGui, QtWidgets
import patientController,EmployeeController,DiseaseController,DepartmentController,DrugController
import RoomController,ServiceController, ScheduleController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(577, 538)
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(200, 170, 281, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(100, 170, 81, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 270, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Patient"))
        self.comboBox.setItemText(1, _translate("Dialog", "Employee"))
        self.comboBox.setItemText(2, _translate("Dialog", "Disease"))
        self.comboBox.setItemText(3, _translate("Dialog", "Department"))
        self.comboBox.setItemText(4, _translate("Dialog", "Drug"))
        self.comboBox.setItemText(5, _translate("Dialog", "Room"))
        self.comboBox.setItemText(6, _translate("Dialog", "Schedule"))
        self.comboBox.setItemText(7, _translate("Dialog", "Service"))
        self.label.setText(_translate("Dialog", "Select Mode :"))
        self.pushButton.setText(_translate("Dialog", "Ok"))

    def show(self):
        self.Dialog.show()

    def on_pushButton_clicked(self):
        selected = str(self.comboBox.currentText())
        if selected == "Patient":
            self.ui = patientController.Ui_Dialog()
            self.ui.show()
            self.Dialog.close()
            
        elif selected == "Employee":
            self.ui = EmployeeController.Ui_Dialog()
            self.ui.show()
            self.Dialog.close()
            
        elif selected == "Disease":
            self.ui = DiseaseController.Ui_Dialog()
            self.ui.show()
            self.Dialog.close()
            
        elif selected == "Department":
            self.ui = DepartmentController.Ui_Dialog()
            self.ui.show()
            self.Dialog.close()
            
        elif selected == "Drug":
            self.ui = DrugController.Ui_Dialog()
            self.ui.show()
            self.Dialog.close()
            
        elif selected == "Room":
            self.ui = RoomController.Ui_Dialog()
            self.ui.show()
            self.Dialog.close()
            
        elif selected == "Schedule":
            self.ui = ScheduleController.Ui_Dialog()
            self.ui.show()
            self.Dialog.close()
            
        elif selected == "Service":
            self.ui = ServiceController.Ui_Dialog()
            self.ui.show()
            self.Dialog.close()

            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
