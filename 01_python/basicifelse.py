# In it when we are using if-else condition, we can write all conditional statement(if-else) without giving any extra space and
# after statement condition we need to give four spaces and then write code like(print cond.)
# this four spaces called 'indentation' which means like in C we use {} for writing multiple code in it but in python 
# we use four spaces instead of {}.

marks = int(input("Enter the marks : "))

if(marks > 100 or marks < 0):
    print("Wrong marks entered")

elif(marks >= 90):
    print("A grade")

elif(marks >= 70 and marks < 90):
    print("B grade")

elif(marks >= 50 and marks < 70):
    print("C grade")

elif(marks >= 35 and marks < 50):
    print("D grade")

else:
    print("E grade")  


#Nested if else

age = int(input("Enter the age : "))

if(age >= 18):
    if(age >= 80):
        print("Cannot Drive")
        print("But can Vote")
    else:
        print("can drive")
        print("can vote also")

else:
    print("not eligible")


list1 = ["apple", "banana"]
if("banana" not in list1):
    print("not in")
else:
    print("in")