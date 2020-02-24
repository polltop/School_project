# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import kuva_rc
import kuva2_rc

from datetime import date, timedelta
from PyQt5.Qt import QBrush, QRect, QPainter, QColor, QListView, QListWidgetItem,\
    QStandardItemModel, QModelIndex
from PyQt5.QtGui import QPaintDevice

#UI_Mainwindów luokka on ohjelman pääikkuna. GUI on toteutettu Qt Designerin avulla ja muutettu .py muotoon. Muunnetun ohjelman sekaan on kirjoitettu omaa koodia.
 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, hotel):
        self.hotel = hotel
        MainWindow.setObjectName("Python B&B")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/photo-1437422061949-f6efbde0a471.jpeg); font: 75 13pt \"Prestige Elite Std\"; color: white;")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 210, 191, 81))
        self.pushButton.setStyleSheet("font: 75 13pt \"Prestige Elite Std\"; border: 1px; border-style: outset; border-color: white; border-radius: 20px; background: transparent;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_customerinfo)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(360, 210, 391, 311))
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("background: transparent; ")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setEnabled(True)
        self.stackedWidgetPage1.setAutoFillBackground(False)
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.customerComboBox = QtWidgets.QComboBox(self.stackedWidgetPage1)
        self.customerComboBox.setGeometry(QtCore.QRect(171, 19, 160, 26))
        self.customerComboBox.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.customerComboBox.setObjectName("customerComboBox")
        self.customerComboBox.addItems(sorted(self.hotel.get_customer_names()))
        self.customerComboBox.setCurrentIndex(0)
        
       
            
        self.customerLabel = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.customerLabel.setGeometry(QtCore.QRect(95, 21, 71, 16))
        self.customerLabel.setStyleSheet("")
        self.customerLabel.setObjectName("customerLabel")
        
        self.dateDateEdit = QtWidgets.QDateEdit(self.stackedWidgetPage1)
        self.dateDateEdit.setGeometry(QtCore.QRect(174, 51, 110, 22))
        self.dateDateEdit.setStyleSheet("border-style: outset; border-width: 1px; border-color: white; border-radius: 5px;\n"
"")
        self.dateDateEdit.setDate(date.today())
        self.dateDateEdit.setObjectName("dateDateEdit")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 48, 27, 27))
        self.pushButton_4.setStyleSheet("border: outset; border-color: white; border-width: 1px; border-radius: 5px; background-image:url(:/newPrefix/muokattu.png)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.open_calendarw)
        
        self.dateLabel = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.dateLabel.setGeometry(QtCore.QRect(127, 51, 39, 16))
        self.dateLabel.setStyleSheet("")
        self.dateLabel.setObjectName("dateLabel")
        self.personsLabel = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.personsLabel.setGeometry(QtCore.QRect(103, 115, 63, 16))
        self.personsLabel.setStyleSheet("")
        self.personsLabel.setObjectName("personsLabel")
        self.personsSpinBox = QtWidgets.QSpinBox(self.stackedWidgetPage1)
        self.personsSpinBox.setGeometry(QtCore.QRect(174, 115, 47, 22))
        self.personsSpinBox.setStyleSheet("border-style: outset; border-width: 1px; border-color: white; border-radius: 5px;\n"
"")
        self.personsSpinBox.setMaximum(4)
        self.personsSpinBox.setMinimum(1)
        self.personsSpinBox.setObjectName("personsSpinBox")
        self.durationSpinBox = QtWidgets.QSpinBox(self.stackedWidgetPage1)
        self.durationSpinBox.setGeometry(QtCore.QRect(174, 83, 47, 22))
        self.durationSpinBox.setStyleSheet("border-style: outset; border-width: 1px; border-color: white; border-radius: 5px;\n"
"")
        self.durationSpinBox.setFrame(True)
        self.durationSpinBox.setObjectName("durationSpinBox")
        self.durationSpinBox.setMinimum(1)
        self.durationLabel = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.durationLabel.setGeometry(QtCore.QRect(32, 83, 141, 16))
        self.durationLabel.setAutoFillBackground(False)
        self.durationLabel.setStyleSheet("")
        self.durationLabel.setObjectName("durationLabel")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.stackedWidgetPage1)
        self.buttonBox.setGeometry(QtCore.QRect(120, 160, 156, 23))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet("border-width: 2px; ")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.make_roomreservation)
        self.buttonBox.rejected.connect(self.cancel_reservationform)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setMouseTracking(False)
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.personsSpinBox_2 = QtWidgets.QSpinBox(self.stackedWidgetPage2)
        self.personsSpinBox_2.setGeometry(QtCore.QRect(176, 113, 47, 22))
        self.personsSpinBox_2.setStyleSheet("border-style: outset; border-width: 1px; border-color: white; border-radius: 5px;")
        self.personsSpinBox_2.setObjectName("personsSpinBox_2")
        self.personsSpinBox_2.setMaximum(4)
        self.personsSpinBox_2.setMinimum(1)
        self.customerLabel_2 = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.customerLabel_2.setGeometry(QtCore.QRect(97, 51, 71, 16))
        self.customerLabel_2.setObjectName("customerLabel_2")
        self.dateDateEdit_2 = QtWidgets.QDateEdit(self.stackedWidgetPage2)
        self.dateDateEdit_2.setGeometry(QtCore.QRect(176, 81, 110, 22))
        self.dateDateEdit_2.setStyleSheet("border-style: outset; border-width: 1px; border-color: white; border-radius: 5px;")
        self.dateDateEdit_2.setDate(QtCore.QDate(2019, 3, 1))
        self.dateDateEdit_2.setObjectName("dateDateEdit_2")
        self.dateDateEdit_2.setDate(date.today())
        self.dateDateEdit_2.setMinimumDate(date.today())
        self.dateLabel_2 = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.dateLabel_2.setGeometry(QtCore.QRect(129, 81, 39, 16))
        self.dateLabel_2.setObjectName("dateLabel_2")
        self.customerComboBox_2 = QtWidgets.QComboBox(self.stackedWidgetPage2)
        self.customerComboBox_2.setGeometry(QtCore.QRect(173, 49, 160, 26))
        self.customerComboBox_2.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.customerComboBox_2.setStyleSheet("")
        self.customerComboBox_2.setObjectName("customerComboBox_2")
        self.customerComboBox_2.addItems(self.hotel.get_customer_names())
        self.customerComboBox_2.setCurrentIndex(0)
        self.personsLabel_2 = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.personsLabel_2.setGeometry(QtCore.QRect(105, 113, 63, 16))
        self.personsLabel_2.setObjectName("personsLabel_2")
        self.serviceLabel = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.serviceLabel.setGeometry(QtCore.QRect(113, 21, 55, 16))
        self.serviceLabel.setObjectName("serviceLabel")
        self.serviceComboBox = QtWidgets.QComboBox(self.stackedWidgetPage2)
        self.serviceComboBox.setGeometry(QtCore.QRect(173, 19, 160, 26))
        self.serviceComboBox.setStyleSheet("")
        self.serviceComboBox.setObjectName("serviceComboBox")
        for service in self.hotel.get_services():
            self.serviceComboBox.addItem(service.get_name())
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.stackedWidgetPage2)
        self.buttonBox_2.setGeometry(QtCore.QRect(120, 200, 156, 23))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.buttonBox_2.accepted.connect(self.make_servicereservation)
        self.buttonBox_2.rejected.connect(self.cancel_reservationform)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
       
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 50, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 40pt \"Prestige Elite Std\"; background: transparent;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 350, 191, 81))
        self.pushButton_3.setStyleSheet("font: 75 13pt \"Prestige Elite Std\"; border: 1px; border-style: outset; border-color: white; border-radius: 20px; background: transparent;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openhistory)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(480, 170, 141, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.comboBox_2.currentIndexChanged.connect(self.room)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
#Alla on apufunktioita painikkeiden käyttöön ja toimenpiteiden tekemiseen

    def room(self):
        self.stackedWidget.setCurrentIndex(self.comboBox_2.currentIndex())

    def open_customerinfo(self):
        self.cust = Customer_Dialog(self, self.hotel)
        
    def open_calendarw(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Calendar_widget()
        self.ui.setupUi(self.Form, self.dateDateEdit, self.hotel)
        
    def openhistory(self):
        self.HistoryWindow = QtWidgets.QWidget()
        self.ui2 = Ui_HistoryWindow()
        self.ui2.setupUi(self.HistoryWindow,self.hotel)
    
    def cancel_reservationform(self):
        self.customerComboBox.setCurrentIndex(0)
        self.dateDateEdit.setDate(date.today())
        self.durationSpinBox.setValue(0)
        self.personsSpinBox.setValue(0)
        self.serviceComboBox.setCurrentIndex(0)
        self.customerComboBox_2.setCurrentIndex(0)
        self.dateDateEdit_2.setDate(date.today())
        self.personsSpinBox_2.setValue(0)
        
    def make_roomreservation(self):
        self.reservation = self.hotel.make_reservation(self.customerComboBox.currentText(), self.comboBox_2.currentText(), self.dateDateEdit.text(), self.durationSpinBox.value())
        message_string = ""
        if self.reservation != False:
            if int(self.durationSpinBox.value()) == 1:
                night = " night is "
            else:
                night = " nights is "
            message_string = "The reservation was succesful! The price for " + str(self.durationSpinBox.value()) + night + str(self.reservation.price) + " euros."
            QtWidgets.QMessageBox.about(self.centralwidget, "Reservation", str(message_string))
        else:
            QtWidgets.QMessageBox.about(self.centralwidget, "Reservation", "The reservation failed!")
        self.customerComboBox.setCurrentIndex(0)
        self.dateDateEdit.setDate(date.today())
        self.durationSpinBox.setValue(0)
        self.personsSpinBox.setValue(0)
        
    def make_servicereservation(self):
        msg = ""
        self.hotel.service_reservation(self.serviceComboBox.currentText(),self.customerComboBox_2.currentText(), self.dateDateEdit_2.text(), self.personsSpinBox_2.value())
        self.serviceComboBox.setCurrentIndex(0)
        self.customerComboBox_2.setCurrentIndex(0)
        self.dateDateEdit_2.setDate(date.today())
        self.personsSpinBox_2.setValue(0)
        msg = str("The reservation for " + self.serviceComboBox.currentText() + " has been made for " + self.personsSpinBox_2.text()+ " persons at " + self.dateDateEdit_2.text())
        QtWidgets.QMessageBox.about(self.centralwidget, "Service reservation", str(msg))
        
        
    def update_all(self):
        names = sorted(self.hotel.get_customer_names())
        self.customerComboBox.clear()
        self.customerComboBox_2.clear()
        self.customerComboBox.addItems(names)
        self.customerComboBox_2.addItems(names)
           

#Qt designerin luoma metodi
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python B&B reservation system"))
        self.centralwidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "New Customer"))
        self.customerLabel.setText(_translate("MainWindow", "Customer:"))
        self.dateDateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.dateLabel.setText(_translate("MainWindow", "Date:"))
        self.personsLabel.setText(_translate("MainWindow", "Persons:"))
        self.durationLabel.setText(_translate("MainWindow", "Duration (nights):"))
        self.customerLabel_2.setText(_translate("MainWindow", "Customer:"))
        self.dateDateEdit_2.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.dateLabel_2.setText(_translate("MainWindow", "Date:"))
        self.personsLabel_2.setText(_translate("MainWindow", "Persons:"))
        self.serviceLabel.setText(_translate("MainWindow", "Service"))
        self.label.setText(_translate("MainWindow", "Python B&B"))
        self.pushButton_3.setText(_translate("MainWindow", "History and statistics"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Room"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Service"))


#Customer_Dialog ikkuna aukeaa new customer painikkeella ja siellä lisätään uusi asiakas.
    
class Customer_Dialog(QtWidgets.QDialog):
    
    def __init__(self, main, hotel):
        super(Customer_Dialog, self).__init__()
        self.form = self.createFormGroupBox()
        self.hotel = hotel
        self.main = main
        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Customer Information")
        self.show()
    
    
    def createFormGroupBox(self):
        self.formGroupBox = QtWidgets.QGroupBox("Fill in your information")
        self.form = QtWidgets.QFormLayout()
        self.name = QtWidgets.QLineEdit()
        self.adress = QtWidgets.QLineEdit()
        self.city = QtWidgets.QLineEdit()
        self.postcode = QtWidgets.QLineEdit()
        self.number = QtWidgets.QLineEdit()
        self.email = QtWidgets.QLineEdit()
        self.form.addRow(QtWidgets.QLabel("Name:"), self.name)
        self.form.addRow(QtWidgets.QLabel("Address"), self.adress)
        self.form.addRow(QtWidgets.QLabel("Postcode:"), self.postcode)
        self.form.addRow(QtWidgets.QLabel("City:"), self.city)
        self.form.addRow(QtWidgets.QLabel("Number:"), self.number)
        self.form.addRow(QtWidgets.QLabel("Email:"), self.email)
        self.formGroupBox.setLayout(self.form)

    def accept(self):
        if len(self.name.text()) == 0 or len(self.adress.text()) == 0 or len(self.city.text()) == 0 or len(self.postcode.text()) == 0 or len(self.number.text()) == 0 or len(self.email.text()) == 0:
            QtWidgets.QMessageBox.about(self.form, "New customer", "Adding a new customer failed. Fill in all of the rows!")
        elif "," in ((self.name.text()) + (self.adress.text()) + (self.city.text()) + (self.postcode.text()) + (self.number.text()) + (self.email.text())):
            QtWidgets.QMessageBox.about(self.form, "New customer", "Adding a new customer failed. No commas are allowed.")
        else:
            self.hotel.add_customer(self.name.text(), self.adress.text()+ " " +self.city.text()+" "+ self.postcode.text(),self.number.text(), self.email.text())
            QtWidgets.QMessageBox.about(self.form, "New customer", "The customer was added succesfully")
        self.close()
        Ui_MainWindow.update_all(self.main)
        

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 230)
        Form.setStyleSheet("background-color: lightblue;")
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Finland))
        self.Calendar = QtWidgets.QCalendarWidget(Form)
        self.Calendar.setGeometry(QtCore.QRect(20, 20, 320, 181))
        self.Calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.Calendar.setObjectName("Calendar")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
    
#Calendar widgetia käytetään pääikunassa päivän valitsemiseen

class Calendar_widget(QPainter):
    def setupUi(self, Form, date_e, hotel):
        self.hotel = hotel
        self.date_e = date_e
        self.form = Form
        self.form.setObjectName("SelectDates")
        self.form.resize(350, 320)
        self.form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Finland))
        self.customerComboBox = QtWidgets.QComboBox(self.form)
        self.customerComboBox.setGeometry(QtCore.QRect(100, 19, 160, 26))
        self.customerComboBox.setObjectName("customerComboBox")
        self.customerComboBox.addItem("Room 1")
        self.customerComboBox.setCurrentIndex(0)
        self.Calendar = QtWidgets.QCalendarWidget(self.form)
        self.Calendar.setGeometry(QtCore.QRect(20, 60, 320, 181))
        self.Calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.Calendar.setObjectName("Calendar")
        buttonBox = QtWidgets.QDialogButtonBox(self.form)
        buttonBox.setGeometry(QtCore.QRect(100, 260, 156, 23))
        buttonBox.setAutoFillBackground(False)
        buttonBox.setStyleSheet("border-width: 2px; ")
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        buttonBox.setCenterButtons(True)
        buttonBox.setObjectName("buttonBox")
        buttonBox.rejected.connect(self.close_file)
        buttonBox.accepted.connect(lambda: self.new_date(self.date_e))
        self.retranslateUi(self.form)
        QtCore.QMetaObject.connectSlotsByName(self.form)
        self.form.show()
        
    def close_file(self):
        self.form.close()
        
    def new_date(self, main):
        self.main = main
        self.form.close()
        self.date_e.setDate(self.Calendar.selectedDate())
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calendar"))
        

#QT Designerin avulla tehty haku/tilastoikkuna hotellin resursseista ja asiakkaista.
class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow, hotel):
        self.hotel = hotel
        HistoryWindow.setObjectName("HistoryWindow")
        HistoryWindow.resize(711, 541)
        HistoryWindow.setMinimumSize(QtCore.QSize(711, 541))
        HistoryWindow.setMinimumSize(QtCore.QSize(711, 541))
        self.radioButton = QtWidgets.QRadioButton(HistoryWindow)
        self.radioButton.setGeometry(QtCore.QRect(60, 80, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(lambda:self.update_list(self.radioButton))
        self.radioButton_2 = QtWidgets.QRadioButton(HistoryWindow)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 80, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(lambda:self.update_list(self.radioButton_2))
        self.radioButton_3 = QtWidgets.QRadioButton(HistoryWindow)
        self.radioButton_3.setGeometry(QtCore.QRect(260, 80, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(lambda:self.update_list(self.radioButton_3))
        self.listView = QtWidgets.QListView(HistoryWindow)
        self.listView.setGeometry(QtCore.QRect(60, 140, 256, 221))
        self.listView.setObjectName("listView")
        self.listView2 = QtWidgets.QListView(HistoryWindow)
        self.listView2.setGeometry(QtCore.QRect(380, 100, 281, 301))
        self.listView2.setObjectName("listView2")
        self.get_statistics()
        self.progressBar = QtWidgets.QProgressBar(HistoryWindow)
        self.progressBar.setGeometry(QtCore.QRect(40, 482, 151, 31))
        self.progressBar.setProperty("value", self.previousr)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximum(self.maxcapacity)
        self.progressBar.setValue(self.previousr)
        self.progressBar_2 = QtWidgets.QProgressBar(HistoryWindow)
        self.progressBar_2.setGeometry(QtCore.QRect(290, 480, 151, 31))
        self.progressBar_2.setProperty("value", self.next_weekr)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_2.setMaximum(self.maxcapacity)
        self.progressBar_2.setValue(self.next_weekr)
        self.progressBar_3 = QtWidgets.QProgressBar(HistoryWindow)
        self.progressBar_3.setGeometry(QtCore.QRect(540, 480, 151, 31))
        self.progressBar_3.setProperty("value", self.next_monthr)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_3.setMaximum(self.monthcapacity)
        self.progressBar_3.setValue(self.next_monthr)
        self.label = QtWidgets.QLabel(HistoryWindow)
        self.label.setGeometry(QtCore.QRect(40, 450, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(HistoryWindow)
        self.label_2.setGeometry(QtCore.QRect(300, 450, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(HistoryWindow)
        self.label_3.setGeometry(QtCore.QRect(544, 450, 131, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(HistoryWindow)
        self.pushButton.setGeometry(QtCore.QRect(150, 380, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(HistoryWindow)
        self.label_4.setGeometry(QtCore.QRect(500, 70, 81, 21))
        self.label_4.setObjectName("label_4")
        self.retranslateUi(HistoryWindow)
        QtCore.QMetaObject.connectSlotsByName(HistoryWindow)
        HistoryWindow.show()

    def retranslateUi(self, HistoryWindow):
        _translate = QtCore.QCoreApplication.translate
        HistoryWindow.setWindowTitle(_translate("HistoryWindow", "History and statistics"))
        self.radioButton.setText(_translate("HistoryWindow", "Customer"))
        self.radioButton_2.setText(_translate("HistoryWindow", "Room"))
        self.radioButton_3.setText(_translate("HistoryWindow", "Service"))
        self.label.setText(_translate("HistoryWindow", "Capacity for previous week"))
        self.label_2.setText(_translate("HistoryWindow", "Capacity for next week"))
        self.label_3.setText(_translate("HistoryWindow", "Capacity for next month"))
        self.pushButton.setText(_translate("HistoryWindow", "Search"))
        self.label_4.setText(_translate("HistoryWindow", "History"))
        
        
#Progressbarien tiedot haetaan tämän funktion sisällä
    def get_statistics(self):
        self.previousr = 0
        self.maxcapacity = len(self.hotel.get_rooms())*7
        self.monthcapacity = len(self.hotel.get_rooms())*30
        self.next_weekr = 0
        self.next_monthr = 0
        for room in self.hotel.get_rooms():
            if room.get_reservations != []:
                for reservation in room.get_reservations():
                    date1 = reservation[0].split("-")
                    start = date(int(date1[0]), int(date1[1]), int(date1[2]))
                    duration = int(reservation[1])
                    if date.today() > start >= (date.today() - timedelta(days = int(7))):
                        self.previousr += duration
                    elif date.today() > (start - timedelta(days = duration)) >= (date.today() - timedelta(days = int(7))):
                        self.previousr += (duration - (((start + timedelta(days = int(duration))) - date.today())).days)
                    if date.today() <= start <= (date.today() + timedelta(days = int(7))):
                        self.next_weekr += duration
                    elif date.today() <= (start - timedelta(days = duration)) <= (date.today() + timedelta(days = int(7))):
                        self.next_weekr += (duration - ((start + timedelta(days = duration) - (date.today() + timedelta(days = 7)))).days)
                    if  date.today() <= start <= (date.today() + timedelta(days = 30)):
                        self.next_monthr += duration
                    elif date.today() <= (start - timedelta(days = duration)) <= (date.today() + timedelta(days = int(30))):
                        self.next_monthr += (duration - ((start + timedelta(days = duration) - (date.today() + timedelta(days = 30)))).days)                            
      
        
#Tietojen tarkastelussa hyödynnetään kahta QlistView widgetiä ja haku laukaistaan search painikkeella.
        
    def update_list(self, radiobutton):
        base = QtGui.QStandardItemModel()
        self.listView.setModel(base)
        self.list = []
        self.currentradio = 0
        if radiobutton == self.radioButton:
            for customer in self.hotel.get_customers():
                row = QtGui.QStandardItem(customer.__str__())
                base.appendRow(row)
                self.list.append(customer)
                self.currentradio = 0
        elif radiobutton == self.radioButton_2:
            for room in self.hotel.get_rooms():
                row = QtGui.QStandardItem(room.__str__())
                base.appendRow(row)
                self.list.append(room)
                self.currentradio = 1
        elif radiobutton == self.radioButton_3:
            for service in self.hotel.get_services():
                row = QtGui.QStandardItem(service.__str__())
                base.appendRow(row)
                self.list.append(service)
                self.currentradio = 2
        self.pushButton.clicked.connect(lambda: self.search(self.listView.currentIndex().row()))
     
    def search(self, index):
        selected = self.list[index]
        self.update_print(selected)
            
        
    def update_print(self, selection):
        base = QtGui.QStandardItemModel()
        self.listView2.setModel(base)
        if self.currentradio == 0:
            if selection.get_all_reservations() != None:
                for reservation in selection.get_all_reservations():
                    row = QtGui.QStandardItem(reservation.__str__())
                    base.appendRow(row)
        elif self.currentradio == 1:
            if selection.get_fullreservations() != None:
                for room in selection.get_fullreservations():
                    row = QtGui.QStandardItem(room.__str__())
                    base.appendRow(row)
        elif self.currentradio == 2:
            if selection.reservations != [] or None :
                for reservation in selection.get_reservations():
                    row = QtGui.QStandardItem(reservation.__str__())
                    base.appendRow(row)
                    
                