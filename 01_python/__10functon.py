# def sum(a, b):
#     s = a + b
#     print(s)
#     return s


# a, b = 5, 4
# sum(a,b)

#factorial of a no. using recursion

# def factorial(n):
#     if n == 0:
#         return 1
#     fact = n * factorial(n-1)
#     return fact

# n = int(input("Enter the no. : "))
# f = factorial(n)
# print(f)

# def num(n):
#     if n == 0:
#         return
#     num(n-1)
#     print(n)


# n = int(input("Enter a no. : "))
# num(n)

# def greaterNo(a, b):
#     if(a>b):
#         print("a is greater")
#     else:
#         print("b is greater")
# a = 4
# b = 3
# greaterNo(a, b)

        # DEFAULT ARGUMENT

# def average(a = 2, b = 8): #default value
#     print("the average is", (a+b)/2)
# average()

# def average(a = 2, b = 4):
#     print("The average is",(a+b)/2)
# average(5) #5 is assined to the a bcz the parameters are default.

# def average(a = 2, b = 4):
#     print("The average is",(a+b)/2)
# average(b = 8)

           # KEYWORD ARGUMENTS
# here order of argument is not necessary
# def average(a = 2, b = 4):
#     print("The average is",(a+b)/2)
# average(b = 6, a = 8)


          # VARIABLE LENGTH ARGUMENTS
# when we don't know no. of inputs. it takes argument as a tuple
# def average(*number):
#     sum = 0
#     for i in number:
#         sum += i #it stores sum of all no.
#     print("the average is : ", sum / len(number))

# average(2,4,9,6,4)

#taking argument as a dictionary
# def ID(**name):
#     print(name["name"], name["Lname"], name["age"])
# dict = {
#     "name" : "Aman",
#     "Lname" : "Bhardwaj",
#     "age" : 19,
# }
# ID(**dict)

def ID(**name):
    print("Hello,", name["fname"], name["lname"])

ID(fname = "Aman", lname = "Bhardwaj")





# def sum(a,b):
#     return a + b
# print(sum(5,8))

def appl(a, value):
    return 6 + a(value)

sum = lambda a, b: a+b
print(sum(7,9))

avg = lambda a,b,c: (a+b+c)/3
print(avg(4,5,7))

sqr = lambda x: x * x
print(sqr(5))

print(appl(sqr, 2))
print(appl(lambda x: x*x*x, 2))
# we can also use lambda fun() as an argument 
