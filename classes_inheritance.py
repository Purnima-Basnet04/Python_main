# Class in python
class A:
    def displayClassA():
        print("Hello User !")
        
# Inheritance in python
class B(A):
    def displayClassB():
        print("this is class B")
        
class C(B):
    def displayClassC():
        print("this is class C")
        
    # creating an instance of class A    
obj = A
#obj.displayClassA()
obj2= B
# obj2.displayClassB()# output: This is class B
# obj2.displayClassA()# output: This is class A inheritedd by class B
obj3= C
obj3.displayClassC()
obj3.displayClassB()
obj3.displayClassA()# output: This is class A inherited by class B inherited by class C