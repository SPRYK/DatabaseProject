import RoomController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(465, 344)
        self.roomid = QtWidgets.QLineEdit(self.Dialog)
        self.roomid.setGeometry(QtCore.QRect(190, 40, 161, 22))
        self.roomid.setObjectName("roomid")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 151, 20))
        self.label.setObjectName("label")
        self.delete_2 = QtWidgets.QPushButton(self.Dialog)
        self.delete_2.setGeometry(QtCore.QRect(100, 280, 93, 28))
        self.delete_2.setObjectName("delete_2")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 131, 20))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(170, 170, 161, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(250, 280, 93, 28))
        self.cancel.setObjectName("cancel")
        self.bedid = QtWidgets.QLineEdit(self.Dialog)
        self.bedid.setGeometry(QtCore.QRect(190, 80, 161, 22))
        self.bedid.setObjectName("bedid")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 151, 20))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(30, 130, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fill = QtWidgets.QPushButton(self.Dialog)
        self.fill.setGeometry(QtCore.QRect(360, 60, 93, 28))
        self.fill.setObjectName("fill")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.delete_2.clicked.connect(self.delete)
        self.cancel.clicked.connect(self.back)
        self.fill.clicked.connect(self.filling)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Delete by Room ID :"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.label_2.setText(_translate("Dialog", "Selected Bed :"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_3.setText(_translate("Dialog", "Delete by Bed ID :"))
        self.fill.setText(_translate("Dialog", "Fill"))


    def show(self):
        self.Dialog.show()


    def delete(self):
        roomID = self.roomid.text()
        bedID = self.bedid.text()
        #TODO add bed to self.textBrowser then delete???
        

        self.ui = RoomController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show() 

    def back(self):
        self.ui = RoomController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show() 


    def filling(self):
        roomID = self.roomid.text()
        bedID = self.bedid.text()
        #TODO add data
        #example
        self.textBrowser.append("bed1")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
