class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count+1

    # def count(self):
    #     print("total object are", self.count)
    
s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()

print("total object are", Student.count)