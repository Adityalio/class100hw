class ATM (object):
    def __init__(self,cardnumber,pin,name,balance):
        self.cardnumber=cardnumber
        self.pin=pin
        self.name=name
        self.balance=balance
        
    def CashWithdraw (self):
        print("Cash Withdraw")
        
    def EnterAmmount (self):
        print("Car is going on with 50 speed")

    def EnterPin(self):
        print("Enter Your Pin")
        
    
aditya=ATM("000009992","4444","Aditya","1000")
print(aditya.EnterPin())