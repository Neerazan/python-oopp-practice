class BankAccount:
    
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposite(self,depositeAmount):
        self.depositeAmount = depositeAmount
        self.balance = self.balance + self.depositeAmount

    def withdrawal(self, withDraw):
        self.withDraw = withDraw
        if(self.withDraw > self.balance):
            print("Insufficient Balance🚨🚨")
        else:
            self.balance = self.balance - self.withDraw
            print("Withdrawal Successfull✅")
    def backFees(self):
        pass

    def display(self):
        print("Account Number: ", self.accountNumber)
        print(" ")
        print("Account Name: ", self.name)
        print(" ")
        print("Account Balance: ", self.balance)

newAccount = BankAccount(123456,"Neerazan",1700000)
newAccount.withdrawal(170034)
print(" ")
newAccount.Deposite(20000)
newAccount.display()