from room import Room
from service import Service
from hotel import Hotel
from calendar import Calendar
import sys
from gui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
    
        

def main():
    rooms = []
    services = [] 
    calendar = Calendar()
    
    #Resources.csv tiedostosta luetaan hotellin tiedot ja alustetaan hotelli.
    
    try:
        file = open("resources.csv", "r")
        for row in file:
            row = row.rstrip()
            splitted = row.split(",")
            if splitted[0] == "Resources":
                pass
            if splitted[0] == "Name":
                hotel_name = splitted[1]
            if splitted[0] == "Room":
                room_number = splitted[1]
                number_of_beds = splitted[2]
                room_price = splitted[3]
                room = Room(room_number, number_of_beds, room_price)
                rooms.append(room)
            if splitted[0] == "Service":
                service_name = splitted[1]
                service_duration = splitted[3]
                service_price = splitted[2]
                service = Service(service_name, service_price, service_duration)
                services.append(service)
    except OSError:
        print("Resource file is broken")
    file.close()
    #Hotelli luodaan keksityn csv-tiedoston pohjalta
    hotel1 = Hotel(hotel_name, rooms, services, calendar)
    
    try:
        load_info = open("customers.csv", "r")
        for event in load_info:
            if event == "":
                break
            elif event == "\n" or len(event) < 4:
                pass
            else:
                event.rstrip()
                list = event.split(",")
                name = list[0].strip(" ")
                adress = list[1]
                number = list[2]
                email = list[3].rstrip()
                if len(list) == 4 and "Spa" not in list[0] and "City-tour" not in list[0]:
                    hotel1.import_customer(name, adress, number, email)
                if len(list) == 4 and ("Spa" in list[0] or "City-tour" in list[0]):
                    cust_name = list[1]
                    date = list[2]
                    persons = list[3]
                    hotel1.import_service(name, cust_name, date, persons)
                if len(list) == 7:
                    rnumber = list[4].strip(" ").split(" ")[2]
                    date = list[5].strip(" ")
                    duration = list[6].split(" ")[0]
                    hotel1.import_reservation_history(name, adress, rnumber, date, duration)             
                    
    except OSError:
        print("Customer file is broken")
    load_info.close()
            
  
    
    global app
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, hotel1)
    MainWindow.show()
    sys.exit(app.exec_())    
    
        
main()
        


    