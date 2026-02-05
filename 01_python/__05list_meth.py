# list is a built in data type that let us create mutable sequence of value
# means in list we can change the value after the declartion of list

list1 = [2, 1, 3]
list2 = [400,300,100]

list1.append(4) #adds one element at the end [2,1,3,4]
print("append",list1)

list1.reverse() #reverse the list [4,3,1,2]
print("reverse list",list1)

list1.sort() #sort in ascending order [1,2,3,4]
print("ascending order",list1)

list1.sort(reverse=True) #sort in descending order[4,3,2,1]
print("descending order",list1)

list1.insert(2,1) #insert element at index (insert(ind,el)) [4,3,1,2,1]
print("insert",list1)

list1.remove(1) #removes first occurence of element [4,3,2,1]
print("remove",list1)

list1.pop(0) #removes element at index [3,2,1]
print("pop",list1)

list1.extend(list2) #Adds another lists end to the current list.
print("extend ",list1)

lst = [1,2,3,4,1,2,1,1]

print(lst.count(1))#counts the occurance of a no.

