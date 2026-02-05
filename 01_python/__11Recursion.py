# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# n = int(input("Enter the no."))
# print(fact(n))

def fibo(n):
    if n <= 0:
        print("incorreect")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    d = fibo(n-1) + fibo(n-2)
    return d
    

n = int(input("Enter the no."))

print(fibo(n))
