def countdown(n):
    while n > 0:
        yield n
        n = n -1
# x is generator object
x = countdown(10)

# next() method
# print(next(x)) #5
# print(next(x)) #4
# print(next(x)) #3
# print(next(x)) #2
# print(next(x)) #1

#for in loop

for num in x :
    print(num)
