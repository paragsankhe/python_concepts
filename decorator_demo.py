#nested function

# def outer(x):
#     def inner(y):
#         return x - y
#     return inner
#
# subtract_six = outer(10)
# result = subtract_six(6)
#
# print(result)

# passing func as an argument

# def multiply(x,y):
#     return(x*y)
#
# def add(x,y):
#     return(x+y)
#
# def calculate(func,x,y):
#     return func(x, y)
#
# result_multiply = calculate(multiply,5,7) #35
# result_addition = calculate(add,10,6) #16
# print(result_addition)

#return function as a value

# def greeting(name):
#     def hello():
#         return ("Hello"+name)
#     return hello
#
# greet = greeting("Jack")
# print(greet())


#python decorators

# def extra_greetings(func):
#     def inner():
#         print("GOod morning")
#         func()
#     return inner
#
# def add_stars(func):
#     def inner():
#         print("********")
#         func()
#     return inner
#
# @add_stars
# @extra_greetings
# def simple_greeting():
#     print("Hello Qtomation")
#
# # decorated_greeting = extra_greetings(simple_greeting)
# # decorated_greeting()
#
# simple_greeting()

def smart_division(func):
    def inner(x,y):
        if (y == 0):
            print("ooops cant divide by 0")
            return inner
        func(x,y)
    return inner

@smart_division
def division(x,y):
    print(x/y)

division(10,5)












