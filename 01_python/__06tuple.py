#A built in data type that lets us create immutable sequences of value
#means we can't change the element after the declaration

# tup[0]=43 #not allowed

#declration of tuple
# tup = () #empty tuple
# tup = (2,) #if we are writing only one element in tuple the comma (,) sign is must to use, whenever it take it as a integer.
# tup = (1,3,2)

tup = (24,21,22,21,20)

print(tup[1:4]) #slicing of tuple

#TUPLE METHODS
print("At index",tup.index(21),",21 is occured first.") #return index of first occurence

print("count",tup.count(21)) #counts total occurences

#reversing a tuple
list = []
for x in reversed(tup):
    list.append(x)
    
print(list)
ntup = tuple(list)
print(ntup)

