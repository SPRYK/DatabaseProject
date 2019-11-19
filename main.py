import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class Database(QDialog):

    def __init__(self):
        super(Database,self).__init__()
        loadUi('main.ui',self)
        self.setWindowTitle("Hospital Database")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label1.setText('Hiii')







if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget=Database()
    widget.show()
    sys.exit(app.exec_())
