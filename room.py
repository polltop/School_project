

class Room:
    def __init__(self, number, beds, price):
        self.room_number = int(number)
        self.beds = int(beds)
        self.price = float(price)
        self.reservations = []
        self.full_reservations = []
        
    def get_reservations(self):
        return self.reservations    
        
    def get_fullreservations(self):
        return self.full_reservations
        
    def get_room_number(self):
        return self.room_number
    
    def get_no_of_beds(self):
        return self.beds
    
    def get_price(self):
        return self.price
    
    def add_reservation(self, date, duration):
        reservation = []
        reservation.append(date)
        reservation.append(duration)
        self.reservations.append(reservation)
        
        
    def add_fullreservation(self, reservation):
        self.full_reservations.append(reservation)
    
    def __str__(self):
        str1 = " Room {:} with {:} beds, {:.2f} euros.".format(self.get_room_number(), self.get_no_of_beds(), self.get_price())
        return str1
        
        