from PyQt5 import QtWidgets, QtCore, QtGui
from hotel import Hotel
from PyQt5.QtWidgets import QGroupBox, QLineEdit, QPushButton, QWidget
from customer import Customer
from PyQt5.Qt import QScreen, pyqtSlot


class GUI(QtWidgets.QMainWindow):
    def __init__(self, hotel):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.hotel = hotel
        self.init_mainwindow()
        self.init_buttons()
        
        
        
    def init_mainwindow(self):
        self.setGeometry(200,200,600,400)
        self.setWindowTitle("{:} reservation system".format(self.hotel.get_name()))
        self.show()
    
    def open_customerinfo(self):
        self.ui = Customer_Dialog(self.hotel)
        
        
        
    def init_buttons(self):
        self.new_customer = QtWidgets.QPushButton("New customer", self)
        self.old_customer = QtWidgets.QPushButton("Reserve a service", self)
        self.make_reservation = QtWidgets.QPushButton("Reserve a room", self)
        self.new_customer.resize(150,100)
        self.new_customer.move(60,150)
        self.new_customer.clicked.connect(self.open_customerinfo)
        self.old_customer.resize(150,100)
        self.old_customer.move(400,150)
        self.make_reservation.resize(150,100)
        self.make_reservation.move(230,150)
        self.new_customer.show()
        self.old_customer.show()
        self.make_reservation.show()
    
        
        

class Customer_Dialog(QtWidgets.QDialog):
    
    def __init__(self, hotel):
        super(Customer_Dialog, self).__init__()
        self.form = self.createFormGroupBox()
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
        self.number = QtWidgets.QLineEdit()
        self.email = QtWidgets.QLineEdit()
        self.form.addRow(QtWidgets.QLabel("Name:"), self.name)
        self.form.addRow(QtWidgets.QLabel("Address/City/Postcode:"), self.adress)
        self.form.addRow(QtWidgets.QLabel("Number:"), self.number)
        self.form.addRow(QtWidgets.QLabel("Email:"), self.email)
        self.formGroupBox.setLayout(self.form)
        self.show()
        
    def accept(self):
        print(self.name.text())
        self.close()
        
    
        

