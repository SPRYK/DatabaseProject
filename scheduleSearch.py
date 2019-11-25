import ScheduleController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(430, 364)
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 40, 91, 20))
        self.label_4.setObjectName("label_4")
        self.workDate = QtWidgets.QDateEdit(self.Dialog)
        self.workDate.setGeometry(QtCore.QRect(180, 90, 110, 22))
        self.workDate.setCalendarPopup(True)
        self.workDate.setObjectName("workDate")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(180, 40, 171, 22))
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 51, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 141, 20))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(170, 160, 201, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(240, 300, 93, 28))
        self.cancel.setObjectName("cancel")
        self.search = QtWidgets.QPushButton(self.Dialog)
        self.search.setGeometry(QtCore.QRect(90, 300, 121, 28))
        self.search.setObjectName("search")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(30, 120, 361, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.search.clicked.connect(self.searching)
        self.cancel.clicked.connect(self.back)          

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
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.search.setText(_translate("Dialog", "Search"))


    def show(self):
        self.Dialog.show()


    def searching(self):
        employID = self.id.text()
        date = self.workDate.date()
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
