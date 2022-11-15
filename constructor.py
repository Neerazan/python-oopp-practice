class Robot:
    
    def introduce_self(self):
        print("my name is "+self.name)

r1 = Robot()
r2 = Robot()

r1.name = "kiley"
r1.color = "White"

r2.name = "kandle"
r2.color = "brown"

r1.introduce_self()
r2.introduce_self()
print(r1.color)
print(r2.color)


# using contructor __init__() function
class car:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def car_properties(self):
        print("The "+self.name+" car has "+self.color+" color and has weight of",self.weight)


c1 = car("Ford","black",123)
c2 = car("mercedes","black",500)

c1.car_properties()
c2.car_properties()

print(c2.color)
print("the weight is %d." %c2.weight)
