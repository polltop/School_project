import unittest
from customer import Customer
from room import Room
from hotel import Hotel
from calendar import Calendar


class TestCriticalFunctions(unittest.TestCase):
    
    def test_customer(self):
        self.customer = Customer("Matti Mallikas","Abc 1 00000 Helsinki","0440000000","matti@mallikas.fi"  )
        self.teststring = "Matti Mallikas, Abc 1 00000 Helsinki, 0440000000, matti@mallikas.fi"
        self.assertEqual(self.customer.__str__(), self.teststring)
    
    #Yksikkötesti kesken
    def test_FailReservation(self):
        self.list1 = []
        self.list2 = []        
        self.calendar = Calendar()
        self.room = Room(2, 2, 60.99)
        self.list1.append(self.room)
        self.hotel = Hotel("Test Hotel",self.list1, self.list2, self.calendar)
        self.cust = self.hotel.add_customer("Matti Mallikas","Abc 1 00000 Helsinki","0440000000","matti@mallikas.fi" )
        self.reservation1 = self.hotel.make_reservation(self.cust, "Room", "15.5.2019", "2")
        
        
    
if __name__ == "__main__":
    unittest.main()

        
    