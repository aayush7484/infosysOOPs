class bank:
    def __init__(self):
        self.balance=50
        print("Account 'A' created")
    def deposit(self):
        amount=int(input("Enter an amount to deposit"))
        self.balance+=amount
        print("Balance=",amount)
    def withdraw(self):
        amount=int(input("Enter an amount to withdraw"))
        if amount>(self.balance-50):
            print("Sorry, minimum balance must be maintained")
        else:
            a=int(self.balance-50-amount)
            print("Balance=",a)
obj1=bank()
obj1.deposit()
obj1.withdraw()
p