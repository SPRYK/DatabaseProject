import MainController,roomAdd,roomAddBed,roomDelete,roomDeleteBed,roomSearch
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.deleteRoom = QtWidgets.QPushButton(self.Dialog)
        self.deleteRoom.setGeometry(QtCore.QRect(230, 30, 141, 28))
        self.deleteRoom.setObjectName("deleteRoom")
        self.searchRoom = QtWidgets.QPushButton(self.Dialog)
        self.searchRoom.setGeometry(QtCore.QRect(130, 90, 141, 28))
        self.searchRoom.setObjectName("searchRoom")
        self.back = QtWidgets.QPushButton(self.Dialog)
        self.back.setGeometry(QtCore.QRect(150, 250, 93, 28))
        self.back.setObjectName("back")
        self.addNewRoom = QtWidgets.QPushButton(self.Dialog)
        self.addNewRoom.setGeometry(QtCore.QRect(30, 30, 141, 28))
        self.addNewRoom.setObjectName("addNewRoom")
        self.deleteBed = QtWidgets.QPushButton(self.Dialog)
        self.deleteBed.setGeometry(QtCore.QRect(200, 170, 141, 28))
        self.deleteBed.setObjectName("deleteBed")
        self.addBed = QtWidgets.QPushButton(self.Dialog)
        self.addBed.setGeometry(QtCore.QRect(50, 170, 141, 28))
        self.addBed.setObjectName("addBed")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.addNewRoom.clicked.connect(self.add_room)
        self.deleteRoom.clicked.connect(self.delete_room)
        self.searchRoom.clicked.connect(self.search_room)
        self.deleteBed.clicked.connect(self.delete_bed)
        self.back.clicked.connect(self.back_main)
        self.addBed.clicked.connect(self.add_bed)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.deleteRoom.setText(_translate("Dialog", "Delete Room"))
        self.searchRoom.setText(_translate("Dialog", "Search Room"))
        self.back.setText(_translate("Dialog", "Back"))
        self.addNewRoom.setText(_translate("Dialog", "Add New Room"))
        self.deleteBed.setText(_translate("Dialog", "Delete Bed"))
        self.addBed.setText(_translate("Dialog", "Add Bed"))


    def show(self):
        self.Dialog.show()


    def back(self):
        self.ui = MainController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def add_room(self):
        self.ui = roomAdd.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def delete_room(self):
        self.ui = roomDelete.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def search_room(self):
        self.ui = roomSearch.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def delete_bed(self):
        self.ui = roomDelete.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()

    def add_bed(self):
        self.ui = roomAddBed.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
