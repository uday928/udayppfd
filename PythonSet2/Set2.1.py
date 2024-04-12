class Bank:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    
    def validate(self,pin):
        PIN=2811
        if PIN==pin:
            return True
        else:
            return False
        
    def display(self):
        n=int(input("enter your pin:"))
        if self.validate(n):
            print("name:"+self.name)
            print("acc_no:"+self.acc_no)
            print("balance:",self.balance)
        else:
            print("enter valid pin")
    
    def deposite(self,amount):
        n=int(input("enter your pin:"))
        if self.validate(n) and amount>0:
            self.balance+=amount
            print(f"{amount} depsoited successfully. current balance: {self.balance}")
        else:
            print("transiction failed")
    
    def withdraw(self,amount):
        n=int(input("enter your pin:"))
        if self.validate(n) and 0<amount<self.balance and self.balance>500:
            self.balance-=amount
            print(f"{amount} withdrwan successfullly. current balance:{self.balance}")
        else:
            print("Transiction failed")

A=Bank("Uday Gandhi","9876543210",10000)
while True:
    n=int(input("1:Account Details,2:Deposite,3:Withdraw,4:exit: "))
    if n==1:
        A.display()
    elif n==2:
        amt=int(input("Enter amount to be deposited: "))
        A.deposite(amt)
    elif n==3:
        amt=int(input("Enter amount to be Withdrawn: "))
        A.withdraw(amt)
    elif n==4:
        break
    else:
        print("Enter valid entry")