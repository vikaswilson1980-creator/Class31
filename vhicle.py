from abc import ABC,abstractmethod
class Vehicle(ABC):
    def maxspeed(self):
        pass
    def color(self):
        pass
    def milage(self):
        pass
class Ferrari(Vehicle):
    def maxspeed(self):
        print("My max speed is 205mph")
    def color(self):
        print("I come in varity of colours")
    def milage(self):
        print("I have a milage of 8.77")
class BMW(Vehicle):
    def maxspeed(self):
        print("My max speed is 185mph")
    def color(self):
        print("I mainly look good in black or white")
    def milage(self):
        print("I have a milage of 6.1")
objFerrari = Ferrari()
objBMW = BMW()
for country in (objFerrari,objBMW):
    country.maxspeed()
    country.color()
    country.milage()