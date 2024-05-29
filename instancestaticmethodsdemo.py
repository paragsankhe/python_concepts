class MyClass:
    def m1(self,name):
        print("inside m1 method",name)
    @staticmethod
    def m2(name):
        print("inside m2 method", name)

p1 = MyClass()
p1.m1("john")

MyClass.m2("jack")