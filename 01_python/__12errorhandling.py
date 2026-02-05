n = input("Enter the no. : ")
try:
    for i in range(1, 11):
        print(f"{n} x {i} = {int(n) * i}")
except:
    print("Invalid data")

#Or we can also use exception as
n = input("Enter the no. : ")
try:
    for i in range(1, 11):
        print(f"{n} x {i} = {int(n) * i}")
except Exception as a:#it automatically gives an error
    print(a)

#Specific type of errors
try:
    num = int(input("Enter a no. "))
    a = [6, 4]
    print(a[num])
except ValueError:
    print("It is not an integer")
except IndexError:
    print("Index Error")

                         
