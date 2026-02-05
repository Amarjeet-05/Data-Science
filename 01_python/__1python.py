print("Hello Aman.", "Hello !")
name = "Aman"
print("The name is : ",name)
a = 2
b = 5
print("the sum of ",a, "and ",b, "is : ", a+b)


#input from user
name = input("enter your name : ")
print(name)
#input always take every value as a string, so for other data type we use input as : 
age = int(input("enter your age :")) #if we didn't write int outside the input it take every value as a string
print(type(age), age)


# Logical operator
val1 = True  #this is the boolean value and it always write with first capital letter(True and False)
val2 = False
print("and operator :", val1 and val2)
print("not operator :", not val1)
print("or operator :", val1 or val2)


#type casting
a = 1
b = "2"
c = int(b) # Here we convert the string data into integer. this is explicitly type conversion.
print(a+c)
print(a + int(b)) # we can also write it in print statement

d = 4.5
print(a+d)#This is called Automatic type conversion in which a is int and d is float it automatically converted the result in float.