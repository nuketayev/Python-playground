from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod

    def go(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    
    def stop(self):
        pass

class Motorcycle(Vehicle):
    
    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        pass



car = Car()
motorcycle = Motorcycle()


car.go()
motorcycle.go()