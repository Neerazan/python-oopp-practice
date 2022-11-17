class Employee:
    def __init__(self, id, salary, department):
        self.ID = id
        self.salary = salary
        self.department = department
    def tax(self):
        return (self.salary * 0.2)
    def salaryPerDay(self):
        return (self.salary / 30)

#initializing the object of the employee class
steve = Employee(11834, 82345, "Engineering")

#printing properties of steve
print("ID = ",steve.ID)
print("salary = ",steve.salary)
print("Department = ",steve.department)
print("Tax paid by steve = ",steve.tax())
print("Salary per day of steve = ", steve.salaryPerDay())
