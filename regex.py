# regex in python 

import re

# pattern for regex 
# pattern = "test"
# string = " This is test string"

# #matching the pattern in the string
# if re.search(pattern, string):
#     print("string found by match method")

# #search
# if re.match(pattern, string):
    # print("string found search method")
    
    
# pattern = r'[a-z]+[a-z]+\d'
# string = input("Enter string: ")


# if re.match(pattern, string):
#     print("pattern matched")
    
# else:
#     print("pattern not matched")
    
pattern = r'[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]'
string = input("Enter your email: ")
if re.match(pattern, string):
    print("valid email")
    print("signed up successfully")
else:
    print("Invalid email")