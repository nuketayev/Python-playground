class Car:
    
    wheels = 4 #class variables
    doors = 5  #class variables

    def __init__(self, marka, model,year,color):
        self.marka = marka #instance variable
        self.model = model #instance variable
        self.year = year   #instance variable
        self.color = color #instance variable

    def drive(self):
        print(self.make+" "+self.model+" is driving")

    def stop(self):
        print(self.make+" "+self.model+" is stopped")



# from car import Car

# Car.wheels = 2
# car_1 = Car("Chevy","Corvey",2021,"blue")
# car_2 = Car("Toyota","Land Cruiser Prado",2003,"Silver metal")


# print(car_1.wheels)
# print(car_2.wheels)