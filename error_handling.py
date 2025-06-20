# Error handling in python

try: # implement the main l;ogic here 
    result = 5/0
    print(result)
    
    
except ZeroDivisionError as e:   # handle the specific error
    print(e) # prints the default message provided by the class
    
    
    
try:
    result = 15/0
    print(result)
    
except ZeroDivisionError as e:
    print ("Error : Division by zero is not allowed") # print the custom message
    
    
try:
    num= int(input("Enter a number: "))
    print (num)
    
except (ValueError, TypeError) as e: # handle multiple exception
    print (e)
class EvenNumberError(Exception):
    pass   
try:
    num1 = int(input("Enter an odd number: "))
    if num1%2 ==0:
        raise ValueError("Error :Number is even") # raise a custom error
    
    else:
        print(num1)
        
except ValueError as e:
    print (e) # priont the custom error message

finally:
    print("finally block executed") # this block of code will be executed regardless