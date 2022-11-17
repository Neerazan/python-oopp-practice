class Employee:

    def __init__(self, id, salary, department):
        self.id = id
        self.salary = salary
        self. department = department

    #method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a = ", a)
        print("b = ", b)
        print('c = ', c)
        print("d = ", d)
        print("e = ", e)

    def tax(self, title = None):
        return (self.salary * 0.2)

    def salayPerDay(self):
        return (self.salary / 30)

steve = Employee(112244, 456789, "engineering")

print("Demo 1")
steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
steve.demo(1, 2, 3, 4, 5)
