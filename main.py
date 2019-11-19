import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class DatabaseUI(QDialog):

    def __init__(self):
        super(DatabaseUI,self).__init__()
        loadUi('main.ui',self)
        self.setWindowTitle("Hospital")
        self.pushButton.clicked.connect(self.on_pushButton_clicked) # Testing

    @pyqtSlot()
    def on_pushButton_clicked(self): # Testing
        self.label1.setText('Hiii')
        while(1):
            print(5)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget=DatabaseUI()
    widget.show()
    sys.exit(app.exec_())
