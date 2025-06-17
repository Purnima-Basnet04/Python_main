#disctionary in python
dict1={
    "name":"pathshala",
    "email": "pathshala@gmail.com",
    "phone": 1234567890,
    "height": 5.8,
}
# print(dict1)# printing the dictionary
# print(dict1.keys())# printing the keys of the dictionary
# print(dict1.values())# printing the values of the dictionary
# print(dict1.items())# printing the items of the dictionary
# print(dict1["email"])#printing the value of key 'email"
#updating values in dictionary
dict1["email"]="pathshala123@gmail.com"
# updating values with update function
dict1.update({"phone": 9876543210})
print("dictionary after updating ", dict1)

#get function in dictionary
print(dict1.get("name")) # printing the value of key 'name'




# for item in dict1.items():
#     print(item)#printing the items of the dictionary
    
# for keys, values in dict1.items():
#     print(keys,values)#printing the items of the dictionary