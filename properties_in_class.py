#creating property inside the class
class Emoployee:
    ID = "NPI000099"
    salary = 80000
    department = "Compuer Engineer"

#creating object
jack = Emoployee()

#printing the property of the jack
print("ID = ", jack.ID)
print("Salary = ", jack.salary)
print("Department = ", jack.department)

print(" ")
print(" ")

#creating property outside the class

class Staff:
    ID = None
    salary = None
    department = None

#creating object
selena = Staff()

#assign values to properties of selena
selena.ID = "NPI000098"
selena.salary = 90000
selena.department = "AI"

# creating property outside the class
selena.title = "senior engineer"

#printing properties of selena
print("ID = ", selena.ID)
print("Salary = ", selena.salary)
print("Department = ", selena.department)
print("Title = ", selena.title)