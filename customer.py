


class Customer:
    def __init__(self, name, adress, number, email):
        self.name = name
        self.adress = adress
        self.number = number
        self.email = email
        self.reservations = []
        
        
    def get_name(self):
        return self.name
    
    def get_adress(self):
        return self.adress
    
    def get_number(self):
        return self.number
    
    def get_email(self):
        return self.email
    
    def get_all_reservations(self):
        new_list = []
        for i in self.reservations:
            new_list.append(i.__str__())
        return new_list
    
    def __str__(self):
        str1 = "{:}, {:}, {:}, {:}".format(self.get_name(), self.get_adress(), self.get_number(), self.get_email())
        return str1
        