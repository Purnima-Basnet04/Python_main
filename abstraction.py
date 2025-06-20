# abstraction in python

from abc import ABC, abstractmethod

class Wallets(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class Paypal(Wallets):
    def pay(self):
        print("Paypal payment successful")
        print("Paypal payment succesfull with amount {amount} via paypal")
        
class khalti(Wallets):
    def pay(self, amount):
        print("khalti payment successfull with amount {amount} via khalti")
        
        
def payment(wallet : Wallets, amount):
    wallet.pay(amount)
    
wallet = input("Enter the wallet name")
amount = float(input("Enter amout to be paid:"))

if wallet.lower() == "paypal":
    payment(Paypal(), amount)
elif wallet.lower() == "khalti":
    payment(khalti(), amount)
else:
    print("\nInvalid wallet name")                
       
        
