def countdown(n):
    while n > 0:
        yield n
        n = n-1

# x is generator object
x = (countdown(5))

# Iterating over the generator object using next
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
