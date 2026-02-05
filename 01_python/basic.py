#dictionary are used to store data values in key:value pairs
#they are ordere, mutable(changeable) & don't allow duplicate keys and indexing are not allowed

dict = {
    "name" : "Aman",
    "age" : 20,
    "class" : "bca",
    "subject" : ["c","cpp","python"]
}

print(dict["subject"])

print(dict["name"])
dict["name"] = "Amarjeet" #here we changed the value of name
print(dict["name"])

dict["surname"] = "Bhardwaj" # initialising new keyvalue
print(dict["surname"])

print(dict)

#so there is also a way to initialise new keywords after making dictionary


ID = {
    1 : "Aman",
    2 : "Anurag",
    3 : "Jishan",
    4 : "Paras",
    5 : "Abhay"
}
#here are two methods of printing value of a key
print(ID[3]) #if this key is not presented in the dictionary it gives us error
print(ID.get(6)) #it not give an error if key is not presented

#Access the keys
print(ID.keys())

#Accessing values
print(ID.values())

for i in ID.keys():
    print(f"value of {i} is {ID[i]}")

print(ID.items())#print key values in the form of list

for key, value in ID.items():
    print(f"Value of {key} is {value}")