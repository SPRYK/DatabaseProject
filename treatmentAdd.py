import patientController, treatmentInpatientAddPopup
from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
password = 'Seth17299004'

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(437, 549)
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 60, 91, 20))
        self.label_4.setObjectName("label_4")
        self.treatmentID = QtWidgets.QLineEdit(self.Dialog)
        self.treatmentID.setGeometry(QtCore.QRect(170, 60, 171, 22))
        self.treatmentID.setObjectName("treatmentID")
        self.makeTreatment = QtWidgets.QPushButton(self.Dialog)
        self.makeTreatment.setGeometry(QtCore.QRect(90, 490, 121, 28))
        self.makeTreatment.setObjectName("makeTreatment")
        self.cancel = QtWidgets.QPushButton(self.Dialog)
        self.cancel.setGeometry(QtCore.QRect(240, 490, 93, 28))
        self.cancel.setObjectName("cancel")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 20, 71, 20))
        self.label_5.setObjectName("label_5")
        self.pid = QtWidgets.QLineEdit(self.Dialog)
        self.pid.setGeometry(QtCore.QRect(170, 20, 171, 22))
        self.pid.setObjectName("pid")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 111, 20))
        self.label_2.setObjectName("label_2")
        self.arriveDate = QtWidgets.QDateEdit(self.Dialog)
        self.arriveDate.setGeometry(QtCore.QRect(200, 100, 110, 22))
        self.arriveDate.setCalendarPopup(True)
        self.arriveDate.setObjectName("arriveDate")
        self.emerMed = QtWidgets.QRadioButton(self.Dialog)
        self.emerMed.setGeometry(QtCore.QRect(230, 150, 81, 20))
        self.emerMed.setObjectName("emerMed")
        self.buttonGroup = QtWidgets.QButtonGroup(self.Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.emerMed)
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 150, 111, 20))
        self.label_6.setObjectName("label_6")
        self.emerLow = QtWidgets.QRadioButton(self.Dialog)
        self.emerLow.setGeometry(QtCore.QRect(320, 150, 81, 20))
        self.emerLow.setObjectName("emerLow")
        self.buttonGroup.addButton(self.emerLow)
        self.emerHigh = QtWidgets.QRadioButton(self.Dialog)
        self.emerHigh.setGeometry(QtCore.QRect(160, 150, 51, 20))
        self.emerHigh.setObjectName("emerHigh")
        self.buttonGroup.addButton(self.emerHigh)
        self.label_8 = QtWidgets.QLabel(self.Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 190, 91, 20))
        self.label_8.setObjectName("label_8")
        self.doctorList = QtWidgets.QComboBox(self.Dialog)
        self.doctorList.setGeometry(QtCore.QRect(180, 190, 141, 22))
        self.doctorList.setObjectName("doctorList")
        self.label_9 = QtWidgets.QLabel(self.Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 230, 121, 20))
        self.label_9.setObjectName("label_9")
        self.diseaseList = QtWidgets.QComboBox(self.Dialog)
        self.diseaseList.setGeometry(QtCore.QRect(180, 230, 141, 22))
        self.diseaseList.setObjectName("diseaseList")
        self.label_10 = QtWidgets.QLabel(self.Dialog)
        self.label_10.setGeometry(QtCore.QRect(100, 270, 71, 20))
        self.label_10.setObjectName("label_10")
        self.drugList = QtWidgets.QComboBox(self.Dialog)
        self.drugList.setGeometry(QtCore.QRect(180, 270, 141, 22))
        self.drugList.setObjectName("drugList")
        self.label_11 = QtWidgets.QLabel(self.Dialog)
        self.label_11.setGeometry(QtCore.QRect(70, 320, 101, 20))
        self.label_11.setObjectName("label_11")
        self.appointList = QtWidgets.QComboBox(self.Dialog)
        self.appointList.setGeometry(QtCore.QRect(180, 320, 141, 22))
        self.appointList.setObjectName("appointList")
        self.label_12 = QtWidgets.QLabel(self.Dialog)
        self.label_12.setGeometry(QtCore.QRect(187, 380, 61, 20))
        self.label_12.setObjectName("label_12")
        self.symptom = QtWidgets.QLineEdit(self.Dialog)
        self.symptom.setGeometry(QtCore.QRect(143, 410, 171, 22))
        self.symptom.setObjectName("symptom")
        self.label_13 = QtWidgets.QLabel(self.Dialog)
        self.label_13.setGeometry(QtCore.QRect(70, 410, 81, 20))
        self.label_13.setObjectName("label_13")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(50, 390, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)


        self.makeTreatment.clicked.connect(self.add)
        self.cancel.clicked.connect(self.back)

        try :
            connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
            print('connected')
            cursor = connection.cursor()
            cursor.execute('select * from employee where Job_Type = \'Doctor\'')
            doctor = cursor.fetchall()
            cursor.execute('select * from disease')
            disease = cursor.fetchall()
            cursor.execute('select * from drug')
            drug = cursor.fetchall()
            cursor.execute('select * from appointment')
            appointment = cursor.fetchall()
            for d in doctor :
                self.doctorList.addItem(d[2])
            for d in disease :
                self.diseaseList.addItem(d[1])
            for d in drug :
                self.drugList.addItem(d[1])
            for a in appointment :
                print(a)
                self.appointList.addItem(str(a[0]))
            print('executed')
            connection.close()
        except Exception as e :
            print(e)

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Treatment ID :"))
        self.makeTreatment.setText(_translate("Dialog", "Make Treatment"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_5.setText(_translate("Dialog", " Patient ID :"))
        self.label_2.setText(_translate("Dialog", "Arrival Date :"))
        self.emerMed.setText(_translate("Dialog", "Medium"))
        self.label_6.setText(_translate("Dialog", "Emergency Level :"))
        self.emerLow.setText(_translate("Dialog", "Low"))
        self.emerHigh.setText(_translate("Dialog", "High"))
        self.label_8.setText(_translate("Dialog", "Assign Doctor :"))
        self.label_9.setText(_translate("Dialog", "Diagnose Disease :"))
        self.label_10.setText(_translate("Dialog", "Use Drug :"))
        self.label_11.setText(_translate("Dialog", "Appointment ID :"))
        self.label_12.setText(_translate("Dialog", "Multivalue"))
        self.label_13.setText(_translate("Dialog", "Symptom :"))


    def show(self):
        self.Dialog.show()


    def add(self):
        patientID = self.pid.text()
        treatmentID = self.treatmentID.text()
        arrivalDate = self.arriveDate.date()
        emergencyLv = ""
        if self.emerHigh.isChecked():
            emergencyLv = "High"
        elif self.emerMed.isChecked():
            emergencyLv = "Medium"
        elif self.emerLow.isChecked():
            emergencyLv = "Low"
        print('pass')
        if len(emergencyLv) == 0 : return None
        assignDoc = str(self.doctorList.currentText())
        diagDisease = str(self.diseaseList.currentText())
        drug = str(self.drugList.currentText())
        appointID = str(self.appointList.currentText())
        symptom = self.symptom.text()

        if treatmentID.upper().startswith("I"):
            self.ui = treatmentInpatientAddPopup.Ui_Dialog(patientID,
                                               treatmentID,
                                               arrivalDate,
                                               emergencyLv,
                                               assignDoc,
                                               diagDisease,
                                               drug, 
                                               appointID)
            self.Dialog.hide()
            self.ui.show()
        else:        
            #TODO add treatment to database
            try :
                connection = mysql.connector.connect(host = 'localhost', database = 'hospital', user = 'root', password = password)
                print('connected')
                cursor = connection.cursor()
                cursor.execute('select * from employee where Employee_Name = \'{}\''.format(assignDoc))
                doctorID = cursor.fetchall()[0][0]
                cursor.execute('select * from disease where Disease_Name = \'{}\''.format(diagDisease))
                diseaseID = cursor.fetchall()[0][0]
                cursor.execute('select * from drug where Drug_Name = \'{}\''.format(drug))
                drugID = cursor.fetchall()[0][0]

                symptoms = [s.strip() for s in symptom.split(',')]
                
                dateinput = '{}-{}-{}'.format(arrivalDate.year(), arrivalDate.month(), arrivalDate.day())
                into = 'Treatment_ID, Patient_ID, Arrival_Date, Emergency_Level, Patient_Type'
                value = '\'{}\', \'{}\', \'{}\', \'{}\', \'{}\''.format(treatmentID, patientID, dateinput, emergencyLv, 0)
                print('insert into {} ({}) value ({})'.format('treatment', into, value))
                cursor.execute('insert into {} ({}) value ({})'.format('treatment', into, value))

                cursor.execute('insert into treatment_assigned_doctor (Treatment_ID, Employee_ID) value (\'{}\', \'{}\')'.format(treatmentID, doctorID))

                cursor.execute('insert into diagnose (Treatment_ID, Disease_ID) value (\'{}\', \'{}\')'.format(treatmentID, diseaseID))

                cursor.execute('insert into used_drug (Treatment_ID, Drug_ID) value (\'{}\', \'{}\')'.format(treatmentID, drugID))

                cursor.execute('insert into correspond_to (Appointment_ID, Treatment_ID) value (\'{}\', \'{}\')'.format(appointID, treatmentID))

                cursor.execute('insert into outpatient (Treatment_ID) value (\'{}\')'.format(treatmentID))

                for s in symptoms :
                    cursor.execute('insert into treatment_symptom (Treatment_ID, Symptom) value(\'{}\', \'{}\')'.format(treatmentID, s))
                
                print('executed')
                connection.commit()
                #result = cursor.fetchall()
                #print(result)
                connection.close()
            except Exception as e :
                print(e)


            #get date by...
            print(arrivalDate.day())
            print(arrivalDate.month())
            print(arrivalDate.year())

            self.ui = patientController.Ui_Dialog()
            self.Dialog.close()
            self.ui.show()            
        
    def back(self):
        self.ui = patientController.Ui_Dialog()
        self.Dialog.close()
        self.ui.show()        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
