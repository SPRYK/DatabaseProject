import ServiceController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 331)
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(190, 130, 161, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.search = QtWidgets.QPushButton(self.Dialog)
        self.search.setGeometry(QtCore.QRect(120, 260, 93, 28))
        self.search.setObjectName("search")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 141, 20))
        self.label_2.setObjectName("label_2")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(270, 260, 93, 28))
        self.cancel.setObjectName("cancel")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(190, 40, 161, 22))
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 161, 20))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(20, 90, 351, 20))
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
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.search.setText(_translate("Dialog", "Search"))
        self.label_2.setText(_translate("Dialog", "Selected Service :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Search by Service ID :"))


    def show(self):
        self.Dialog.show()


    def searching(self):
        serviceID = self.id.text()
        #TODO add service to self.textBrowser
        
        #example
        self.textBrowser.append("service1")
        
        

    def back(self):
        self.ui = ServiceController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
