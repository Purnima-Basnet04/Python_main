#list in python

list1 = ['Hello', 'world', 'python' ,'programming',1,2.4, True,None,"Hello"]
list2=[5,8,11,20,34,49,1]
#print(list1) # printing whole list
#print(list1[1])#printing through index
#print(list[2:5])#printing through index range
#print(list1[ :5]) #printing through index range from start to 5
#print(list1[5: ])#printing from index 5 to end
#list.append ('Append string')
#print(list1)
#print(len(list1))
#list1.reverse()# reversing the list
#print(list1, end=" ") # printing reversed list
#list1. remove(2.4)
#print(list1)
#list1.pop()
#print(list1)

#list2.sort()
#print("sorted list: ", list2) #shorting the list in ascending order")

list2.sort(reverse=True)
#print("sorted list: ", list2) #shorting the list in descending order")

list2.insert(2,10) #inserting element at index 2print (list2)

#for clearing list 
list2.clear()
#print(list2)

# printing using len function
#for i in range (len(list1)):
    #print(list1[i], end= " ")
    
    
#printing every items in list using for loop
#for item in list1:
     #print(item, end=" ")
print(list1+list2)