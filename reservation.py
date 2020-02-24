from calendar import Calendar
from room import Room
from service import Service



class Reservation:
    def __init__(self, hotel, customer, rtype, date, duration, room):
            self.hotel = hotel
            self.customer = customer
            self.date = date
            self.rtype = rtype
            self.duration = int(duration)
            self.roomnumber = room.get_room_number()
            self.price = self.duration*(room.get_price())
                            
                            
                        
    def __str__(self):
        str1 = "{:}, {:} number {:}, {:} ,{:} nights.".format(self.customer, self.rtype, self.roomnumber, self.date, self.duration)
        return str1
    