class Car:

    def start(self):
        print("This car is starting")
        return self

    def drive(self):
        print("This car is driving")
        return self

car = Car()

car.start()\
    .drive()