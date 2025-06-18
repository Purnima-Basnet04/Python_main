#functions in python



#function with no arguments and no return value
def displayHelloWorld():
    print("Hello, World!")
    
#function with no argument and return value
def add():
    num1 =10
    num2 = 20
    sum = num1 + num2
    return sum

#function with arguments and no return value
def displayName(name):
    print("Hello, " + name +"!")

# function with arguments and return value
def displayData(num1, num2):
    prod = num1*num2 
    return prod



displayHelloWorld()
result = add()+10
print(result)

name="john"
displayName(name)

result1 =displayData (5, 6)
print("The producrts of 5 and 6 is :", result1)