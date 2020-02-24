


class Service:
    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration
        self.reservations = []
        
    def get_reservations(self):
        return self.reservations
    
    def add_reservation(self, s_name, customer, date, persons):
        list = []
        list.append(s_name)
        list.append(customer)
        list.append(date)
        list.append(persons)
        self.reservations.append(list)
    
        
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_duration(self):
        return self.duration
    
    def __str__(self):
        str1 = "{:} takes {:} hours and costs {:} euros.".format(self.get_name(), self.duration, self.get_price())
        return str1