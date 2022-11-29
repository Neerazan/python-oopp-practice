
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("length: ",self.length)
        print("Width: ",self.width)
        print("Area: ",self.area())
        print("perimeter: ",self.perimeter())

area1 = Rectangle(4,5)
area1.display()
