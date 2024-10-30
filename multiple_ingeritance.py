class Prey:
    
    def flee(self):
        print("This animal is flees")

class Predator:
    
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()

