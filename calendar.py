from datetime import date, time, timedelta
from room import Room



class Calendar:
    
    
    def __init__(self):
        self.today = date.today()
        self.limit = self.today + timedelta(weeks = 12)      
        
    def get_llimit(self):
        return self.today
    
    def get_hlimit(self):
        return self.limit
    
    def check_dates(self, room, r_date, duration):
        i = 0
        j = 0
        reservations = room.get_reservations()
        for reservation in reservations:
            date1 = r_date.split("-")
            a_date = date(int(date1[0]), int(date1[1]), int(date1[2]))
            b_date = a_date + timedelta(days = int(duration))
            r1_date = reservation[0].split("-")
            c_date = date(int(r1_date[0]), int(r1_date[1]), int(r1_date[2]))
            d_date = c_date + timedelta(days = int(reservation[1]))
            if self.today <= a_date <= self.limit and self.today <= b_date <= self.limit:
                j += 1
                if (c_date < a_date and d_date <= a_date) or (c_date >= b_date and d_date > b_date):
                    i += 1
                    
                    
        if i != len(room.get_reservations()) or j == 0:
            return False
        else:
            return True
            
    
    
    
    
