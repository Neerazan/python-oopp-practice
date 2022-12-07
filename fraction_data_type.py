class Fraction:
    
    
    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self):
        return "{}/{}".format(self.num,self.den)


    #here self will get fr1 and other will get fr2
    def __add__(self,other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den
        return "{}/{}".format(new_num,new_den)

    def __sub__(self,other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        return "{}/{}".format(new_num,new_den)

    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return "{}/{}".format(new_num,new_den)

    def __truediv__(self,other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return "{}/{}".format(new_num,new_den)

    def convert_to_decimal(self):
        return self.num/self.den

fr1 = Fraction(3,4)
fr2 = Fraction(1,2)
print("addition")
print(fr1+fr2)
print(" ")
print("substraction")
print(fr1-fr2)
print(" ")
print("multiplication")
print(fr1*fr2)
print(" ")
print("division")
print(fr1/fr2)
print(" ")
print("decimal")
print(fr1.convert_to_decimal())
