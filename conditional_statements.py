# conditional statements in python

#num1 = int(input("Enter first number"))
#num2 = int(input("Enter second number"))
#if num1 ==0:
   # print(f"{num1} is zero")
#if num1 %2 ==0:
  #  print("Number is even")
#else:
    #print(f"{num1} is odd number.")   
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int (input("Enter third number: "))
    
if num1>num2:
        if num1>num3:
            print(f"{num1} is greater than {num2} and {num3}")
elif num2>num1 and num2>num3:
        print(f"{num2} is greater than {num1} and {num2}")
else:
        print(f"{num3} is greater than {num1} and {num2}")    
        