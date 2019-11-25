import DiseaseController
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(422, 302)
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(160, 20, 171, 22))
        self.id.setObjectName("id")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 70, 101, 20))
        self.label_5.setObjectName("label_5")
        self.name = QtWidgets.QLineEdit(self.Dialog)
        self.name.setGeometry(QtCore.QRect(160, 70, 171, 22))
        self.name.setObjectName("name")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(230, 250, 93, 28))
        self.cancel.setObjectName("cancel")
        self.ok = QtWidgets.QPushButton(self.Dialog)
        self.ok.setGeometry(QtCore.QRect(80, 250, 121, 28))
        self.ok.setObjectName("ok")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 131, 20))
        self.label_6.setObjectName("label_6")
        self.specialty = QtWidgets.QTextEdit(self.Dialog)
        self.specialty.setGeometry(QtCore.QRect(170, 170, 201, 31))
        self.specialty.setObjectName("specialty")
        self.label_10 = QtWidgets.QLabel(self.Dialog)
        self.label_10.setGeometry(QtCore.QRect(167, 120, 61, 20))
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(30, 130, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.ok.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", " Disease ID :"))
        self.label_5.setText(_translate("Dialog", " Disease Name :"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.label_6.setText(_translate("Dialog", " Disease Specialty :"))
        self.label_10.setText(_translate("Dialog", "Multivalue"))


    def show(self):
        self.Dialog.show()


    def add(self):
        diseaseID = self.id.text()
        diseaseName = self.name.text()
        diseaseDesc = self.specialty.toPlainText()
        #TODO add disease to database
        
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital',
                                                 user='root',
                                                 password='root')
            objdata = (diseaseID, diseaseName)
            
            sqlQuery = "insert into "+"disease"+"(Disease_ID, Disease_Name) " \
                            "values(%s,%s)"

            temp_list = list(objdata)

            
            #for int
            if(diseaseName == ""):
                temp_list.remove(diseaseName)
                sqlQuery=sqlQuery.replace(", Disease_Name",'')
                sqlQuery=sqlQuery.replace("%s,",'',1)

            objdata = tuple(temp_list)
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
        except Exception as e:
            retmsg = ["1", "writing error"]
            print(e)
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                
        #add disease_specialty
        try:
            connection = mysql.connector.connect(host='localhost',database='hospital',user='root',password='root')
            sqlQuery = "insert into "+"disease_specialty"+"(Disease_ID, Specialty) "+"values(%s,%s)"

            for desc in diseaseDesc.split():
                objdata = (diseaseID,desc)
                cursor = connection.cursor()
                cursor.execute(sqlQuery, objdata)
                connection.commit()
            
        except Exception as e:
            retmsg_s = ["1", "writing error"]
            print(e)
            print("Fetch Error")
        else :
            retmsg_s = ["0", "writing done"]
        finally :
            try:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
            except Exception as e:
                print(e)
        
        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()

        
    def back(self):
        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()         

    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
