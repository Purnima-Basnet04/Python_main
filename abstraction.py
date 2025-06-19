# abstraction in python

from abc import ABC, abstractmethod

class Wallets(ABC):
    @abstractmethod
    def pay():
        print ("Test")
    
obj = Wallets
obj.pay()