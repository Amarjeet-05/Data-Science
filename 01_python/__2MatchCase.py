# Match case is just like a Switch condition which we are using in C. In it break statement
# is not neccesary just like C.

n = int(input("Enter the x : "))
match n:
    case 1:            #if n is 1
        print(n)

    case _ if(n > 1 and n<5):
        print(n)

    case _:            #default
        print("er")