# def myfunc(x, y, z):
#     print(x, y, z)
#
# # myfunc(100, 200, 300) #positional arguments
#
# # myfunc(x =100, y=200, z=300) #keyword args
# myfunc(z =300, x =100, y= 200)

# def myfunc(name, country = "India"):
#     print(name , country)
#
# myfunc("jack", "Norway")
# myfunc("jack")
# myfunc("john")


# def myfunc(x, y, z):
#     print(x, y, z)
#
# myfunc(100, 200, 300) #positional args : valid
# myfunc(x=100, y=200, z=300) #keyword args : valid
# myfunc(y=200, z=300, x=100) #keyword args : valid
# myfunc(100, 200, z=300) #combination of positional and keyword args valid
# myfunc(100, y = 200, z=300) #combination of positional and keyword args valid
# myfunc(100, y = 200, 300) #invalid :positional args should be always before keyword args



def myfunc(*kids):
    print(kids)
    print(kids[1])

myfunc("john","jack","jenny")
















