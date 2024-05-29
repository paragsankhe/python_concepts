class MyClass:
    def __init__(self):
        print("this is inside constructor")

    def m1(self):
        print("this is m1 method")

    def m2(self,num1,num2):
        return(num1+num2)

myobj = MyClass()
myobj.m1()
result = myobj.m2(10,20)
print(result)

