count = 1
while count <= 3:
    print(count)
    count += 1


# for loop are used for list, tuples,string. and there is no increament statement will used.

list = [1,2,3,4,5,6]

for val in list:
    print(val)



# range functions returns a sequence of numbers, starting from 0 by default, and increament by 1(by default), and stops before specific number.
# range(start?, stop, step?) here ? is represented by optional and steps represented by increament or decreament(-1) value.
# it was just like [for(int i = 0; i < n; i++)].

for i in range(3): #[range(stop)]
    print(i)

for i in range(1, 3): #[range(start, stop)]
    print(i)

for i in range(1, 5, 2): #[range(start, stop, step)]
    print(i)
