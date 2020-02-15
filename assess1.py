class bank:
    def __init__(self):
        self.balance=0
        print("Account 'A' Created")
    def deposit(self):
        amount=int(input("Enter an amount to Deposit"))
        self.balance+=amount
        print("Balance=",self.balance)
    def withdraw(self):
        amount=int(input("Enter an amount tp Withdraw"))
        a=int(amount-self.balance)
        if amount>self.balance:
            print("Insufficient Fund of",a)
        else:
            self.balance-=amount
            print("Balance=",self.balance)
a1=bank()
a1.deposit()
a1.withdraw()

