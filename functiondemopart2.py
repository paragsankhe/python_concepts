# myvar1 = 100 #global variable
#
# def myfunc():
#     myvar2 = 200 #local varibale
#     print(myvar2)
#     print(myvar1)
#
# myfunc()
#
# print(myvar1)
# print(myvar2)

# abc = 100 #global variable
#
# def myfunc():
#     abc = 200 #local variable
#     print(abc)
#
# myfunc()
# print(abc)

# abc = 100
#
# def myfunc():
#     global abc
#     abc =300
#     print(abc)
#
# myfunc()
# print(abc)

# abc = 100 # global variable
#
# def myfunc():
#     global abc
#     abc = 200
#     print(abc)
#
# print(abc)

def myfunc():
    global abc
    abc = 200
    print(abc)

myfunc()
print(abc)










