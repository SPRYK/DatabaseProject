import DepartmentController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(457, 504)
        self.search = QtWidgets.QPushButton(self.Dialog)
        self.search.setGeometry(QtCore.QRect(80, 450, 93, 28))
        self.search.setObjectName("search")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(180, 130, 241, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 161, 20))
        self.label.setObjectName("label")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(230, 450, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 141, 20))
        self.label_2.setObjectName("label_2")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(200, 40, 161, 22))
        self.id.setObjectName("id")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 80, 391, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        
        self.cancel.clicked.connect(self.back)
        self.search.clicked.connect(self.searching)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search.setText(_translate("Dialog", "Search"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "Search by Department ID :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Selected Department :"))


    def show(self):
        self.Dialog.show()


    def back(self):
        self.ui = DepartmentController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()

    def searching(self):
        departID = self.id.text()
        #TODO add depart to self.textBrower
        
        #example
        self.textBrowser.append('depart1')
        self.textBrowser.append('depart2')
        self.textBrowser.append('depart3')        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
