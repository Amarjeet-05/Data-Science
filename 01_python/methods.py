id1 = {1 : "Aman", 2 : "Anurag", 3 : "Abhay"}
id2 = { 4 : "Jishan", 5 : "Paras", 6 : "Himanshu"}

id1.update(id2)  
print(id1)

id2.clear() #clear all the elements from dictionary
print(id2)

#removes key value pair
id1.pop(6)
print(id1)

#Removes last item from the dictionary
id1.popitem()
print(id1)

#delete the dictionary 
del id2

id2 = { 4 : "Jishan", 5 : "Paras", 6 : "Himanshu"}
                            

