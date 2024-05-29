#multiple objects creation from class

# class MyClass:
#
#     def mymethod(self):
#         print("hello world")
#
# myobj1 = MyClass()
# myobj1.mymethod()
#
# myobj2 = MyClass()
# myobj2.mymethod()

#checking  memory location of objects

class MyClass:
    def printname(self):
        print("myname")

myobj1 = MyClass() #named object
myobj2 = MyClass()
myobj3 = myobj1

print(myobj1 is myobj2) #False
print(myobj1 is myobj3) #True

print(myobj1 is not myobj2) #True
print(myobj1 is not myobj3) #Flase


















