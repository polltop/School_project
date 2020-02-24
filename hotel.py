from customer import Customer
from room import Room
from service import Service
from reservation import Reservation

#Hotel-luokka on ns. ohjelman ydin johon lis‰t‰‰n kaikki asiakkaat ja varaukset.
class Hotel:
    def __init__(self, name, rooms, services, calendar):
        self.name = name
        self.rooms = rooms
        self.services = services
        self.calendar = calendar
        self.customer_names = []
        self.customers = []
        self.reservations = []
        
    def add_customer(self, name, adress, number, email):
        customer = Customer(name, adress, number, email)
        self.customers.append(customer)
        self.customer_names.append(name)
        self.save(customer.__str__())
        return customer
        
    def make_reservation(self, customer, rtype, date, duration):   
        date_s = date.split(".")
        date = date_s[2]+"-"+date_s[1]+"-"+date_s[0]
        for i in self.customers:
            if i.get_name() == customer or customer == i:
                customer_c = i
        a = 0
        b = 0     
        #Huoneen varaus/paivien testaus for-loopilla. Calendar-luokan check-dates metodissa k‰yd‰‰n l‰pi huonekohtaiset varaukset.
        if "Room" in rtype:
            for room in self.get_rooms():
                a += 1
                if room.get_reservations() == []:
                    room.add_reservation(date, duration)
                    roomnumber = room.get_room_number()
                    reservation = Reservation(self, customer_c, rtype, date, str(duration), room)
                    self.reservations.append(reservation)
                    customer_c.reservations.append(reservation)
                    room.add_fullreservation(reservation)
                    self.save(reservation.__str__())
                    return reservation
                else:
                    if self.calendar.check_dates(room, date, duration) == True:
                        b += 1
                        room.add_reservation(date, duration)
                        reservation = Reservation(self, customer_c, rtype, date, str(duration), room)
                        self.reservations.append(reservation)
                        customer_c.reservations.append(reservation)
                        self.save(reservation.__str__())
                        room.add_fullreservation(reservation)
                        return reservation
                    elif a == len(self.get_rooms()) and b == 0:
                        return False
    
    def service_reservation(self, s_name, customer, date, persons):
        for service in self.services:
            if service.get_name() == s_name:
                service.add_reservation(s_name, customer, date, persons)
                save_str = str(s_name+ "," + customer+ "," + date + "," + str(persons))
        self.save(save_str)
        
    def import_service(self, s_name, customer, date, persons):
        list = []
        list.append(s_name)
        list.append(customer)
        list.append(date)
        list.append(persons)
        for service in self.services:
            if service.get_name() == s_name:
                service.reservations.append(list)
        
       
    def save(self, i):        
        file1 = open("customers.csv", "a+")  
        if ("Spa" or "City-tour") in i:
            file1.write(i)
        else:
            file1.write(i.__str__())
            file1.write("\n")
            file1.close()
        
    #Import funktiot on suunniteltu ainoastaan tiedostosta luontia varten.    
    def import_customer(self, name, adress, number, email):
        customer = Customer(name, adress, number, email)
        self.customers.append(customer)
        self.customer_names.append(name)
        
    def import_reservation_history(self, name, adress, number, date, duration):
        for cust in self.customers:
            if name in cust.__str__() and adress in cust.__str__():
                for room in self.rooms:
                    if room.get_room_number() == int(number):
                        room.add_reservation(date, duration)
                        reservation = Reservation(self, cust, "Room", date, str(duration), room)
                        self.reservations.append(reservation)
                        cust.reservations.append(reservation)
                        room.add_fullreservation(reservation)
            else:
                pass
                    
        
        
    def get_customers(self):
        return self.customers
    
    def get_customer_names(self):
        return self.customer_names
    
    def get_name(self):
        return self.name
        
    def get_rooms(self):
        return self.rooms
    
    def get_services(self):
        return self.services
    
        