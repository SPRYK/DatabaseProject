from PyQt5 import QtCore, QtGui, QtWidgets
import ScheduleController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 40, 91, 20))
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(180, 90, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 40, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 51, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 141, 20))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(180, 140, 161, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 230, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 121, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.back)          

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", " Employee ID :"))
        self.label_2.setText(_translate("Dialog", " Date :"))
        self.label_3.setText(_translate("Dialog", "Selected Schedule :"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Cancel"))


    def show(self):
        self.Dialog.show()

    def search(self):
        employID = self.lineEdit_2.text()
        date = self.dateEdit.date()
        #TODO add Schedule to self.textBrowser
        
        #get date by...
        print(date.day())
        print(date.month())
        print(date.year())
        #example
        self.textBrowser.append("schedule1")
        self.textBrowser.append("schedule2")
        self.textBrowser.append("schedule3")

        
    def back(self):
        self.ui = ScheduleController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
