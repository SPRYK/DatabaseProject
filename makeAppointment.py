from PyQt5 import QtCore, QtGui, QtWidgets
import patientController,EmployeeController,DiseaseController,DepartmentController,DrugController
import RoomController,ServiceController, ScheduleController
import datetime
import mysql.connector

### all connection details are declared here ###
host = 'localhost'
database = 'hospital'
user = 'root'
password = 'Seth17299004'

### utility functions ###
def constructTable(dialog, callback) :
    table = QtWidgets.QTableWidget(dialog)
    table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
    table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
    table.selectionModel().selectionChanged.connect(callback)
    return table
def populateTable(table, columns, rows) :
    table.setColumnCount(len(columns))
    table.setRowCount(len(rows))
    for j in range(len(columns)) :
        table.setHorizontalHeaderItem(j, QtWidgets.QTableWidgetItem(str(columns[j])))
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        for i in range(len(rows)) :
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(rows[i][j])))

class dialog:
    width = 1280
    height = 720
    def __init__(self):
        # dialog
        self.dialog = QtWidgets.QDialog()
        self.dialog.setWindowTitle('dialog')
        self.dialog.resize(self.width, self.height)
        # patientTable
        self.patientTable = constructTable(self.dialog, self.onPatientSelected)
        self.patientTable.setGeometry(0, 0, 1280, 360 - 15)
        # doctorTable
        self.doctorTable = constructTable(self.dialog, self.onDoctorSelected)
        self.doctorTable.setGeometry(0, 360 + 15, 480, 360 - 15)
        # scheduleTable
        self.scheduleTable = constructTable(self.dialog, self.onScheduleSelected)
        self.scheduleTable.setGeometry(480, 360 + 15, 240, 360 - 15)
        # labels
        self.patientLabel = QtWidgets.QLabel(self.dialog)
        self.patientLabel.setGeometry(1000, 360 + 15, 100, 100)
        self.patientLabel.setText('Patient')
        self.doctorLabel = QtWidgets.QLabel(self.dialog)
        self.doctorLabel.setGeometry(1000, 360 + 15 + 50, 100, 100)
        self.doctorLabel.setText('Doctor')
        self.scheduleLabel = QtWidgets.QLabel(self.dialog)
        self.scheduleLabel.setGeometry(1000, 360 + 15 + 100, 100, 100)
        self.scheduleLabel.setText('Schedule')
        # insertButton
        self.insertButton = QtWidgets.QPushButton(self.dialog)
        self.insertButton.setGeometry(1000, 360 + 15 + 200, 120, 30)
        self.insertButton.setText('Insert')
        self.insertButton.clicked.connect(self.onInsertButtonClicked)
        # finalize
        self.queryData()
        self.dialog.show()
    def queryData(self) :
        connection = mysql.connector.connect(host = host, database = database, user = user, password = password)
        cursor = connection.cursor()
        # patient
        patientColumns = ['Patient ID', 'National ID', 'Patient name', 'Gender', 'Date of birth', 'Blood group', 'Status']
        cursor.execute('select * from hospital.patient')
        patientRows = cursor.fetchall()
        populateTable(self.patientTable, patientColumns, patientRows)
        # doctor
        doctorColumns = ['Employee ID', 'Doctor name', 'Department']
        cursor.execute('''select emp.Employee_ID, emp.Employee_Name, dept.Dept_Name
from employee emp
inner join doctor doc on emp.Employee_ID = doc.Employee_ID
inner join department dept on emp.Dept_ID = dept.Dept_ID''')
        doctorRows = cursor.fetchall()
        populateTable(self.doctorTable, doctorColumns, doctorRows)
        connection.close()
    def onInsertButtonClicked(self) :
        print('insert')
        # TODO insert sql
    def onPatientSelected(self) :
        #print(self.patientTable.currentRow())
        #print(self.patientTable.item(self.patientTable.currentRow(), 0).text())
        self.patientLabel.setText(self.patientTable.item(self.patientTable.currentRow(), 2).text())
    def onDoctorSelected(self) :
        self.doctorLabel.setText(self.doctorTable.item(self.doctorTable.currentRow(), 1).text())
        connection = mysql.connector.connect(host = host, database = database, user = user, password = password)
        cursor = connection.cursor()
        scheduleColumns = ['Date', 'Time']
        cursor.execute('select Work_Date, Start_time from schedule where Employee_ID = {}'.format(self.doctorTable.item(self.doctorTable.currentRow(), 0).text()))
        scheduleRows = cursor.fetchall()
        populateTable(self.scheduleTable, scheduleColumns, scheduleRows)
        connection.close()
    def onScheduleSelected(self) :
        s0 = self.scheduleTable.item(self.scheduleTable.currentRow(), 0).text()
        s1 = self.scheduleTable.item(self.scheduleTable.currentRow(), 1).text()
        print('pass')
        self.scheduleLabel.setText('{} {}'.format(s0, s1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = dialog()
    sys.exit(app.exec_())
