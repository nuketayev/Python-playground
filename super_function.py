class Rectangule:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangule):
    
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width

class Cube(Rectangule):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return  self.width*self.height*self.length
    

square = Square(3,3)
cube = Cube(3,3,3)

print("The area of the square is: "+str(square.area()))
print("The volume of the cube is: "+str(cube.volume()))

