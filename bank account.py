class BankAccount:
    def __init__(self,name,no):
        self.account_holder_name=name
        self.account_number=no
        self.current_balance=0
    def deposit(self,amt):
        if(amt<1):
            print("enter valid domination")
        else:
            self.current_balance +=amt
            print(amt," successfully deposited")
    def withdraw(self,amt):
        if(amt<=self.current_balance):
            self.current_balance -=amt
            print("You withdrawed",amt)
        else:
            print("Insufficient balance")
    def currentbalance(self):
        print("Account Holder Name:",self.account_holder_name)
        print("Account Number:",self.account_number)
        print("Balance:",self.current_balance)

obj=BankAccount("Sir","0023036748")
obj.currentbalance()
obj.deposit(5000)
obj.withdraw(2000)
obj.currentbalance()
