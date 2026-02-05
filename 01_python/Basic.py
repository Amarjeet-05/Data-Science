#Set are unorder specific value which are immutable. Duplication of values and indexing are not allowed

name = {"Sia", "Ria", "Mia"}
name2 = {"Monny", "Tonny", "Sonny"}

#checking the item is presented
if "Sia" in name:
    print("Presented")

#add elements to the set
name.add("Tia")
print(name)

#Add another sequence of Set
name.update(name2)
print(name)

#removing element from set
name.remove("Tia")
print(name)

#discard/remove element(it will not throw an error if element is not present)
name.discard("Jia")
print(name)

#Joining 2 sets
s1 = {'a', 'b', 'c'}#'a' is print only one time bcz duplication is not allowed
s2 = {'d', 'e', 'a'}
s3 = s1.union(s2)
print(s3)

#keep duplicates while joining
s1.intersection_update(s2)
print(s1)

s4 = {1,2,3,4,5}
s5 = {1,5,7,8,9}

#keep all values except duplicats
s4.symmetric_difference_update(s5)
print(s4)

#returns true when there is no common value
a = {1,2,3,4,5,7}
b = {8,9,10,11,0}
print(a.isdisjoint(b))

