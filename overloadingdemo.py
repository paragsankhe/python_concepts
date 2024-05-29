# class A:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
#
# myobj = A()
# myobj.add(2,4) #6
# myobj.add(100) #100
# myobj.add(1,2,30) #33

# class A:
#     def add(self,a=None,b=None):
#         if a!=None and b==None:
#             print(a)
#         else:
#             print(a+b)
# myobj = A()
# myobj.add(100,200) #300
# myobj.add(400) #400

# mulitiple dispatch

from multipledispatch import dispatch
class A:
    @dispatch(int, int)
    def add(self,a,b):
        print(a+b)

    @dispatch(int)
    def add(self,a):
        print(a)

    @dispatch(int, int, int)
    def add(self, a, b, c):
        print(a + b + c)

    @dispatch(float,float,float,float)
    def add(self, a, b, c,d):
        print(a + b + c + d)

myobj = A()
myobj.add(2,5,7) #14
myobj.add(100) #100
myobj.add(200,400) #600
myobj.add(2.5,5.3,6.2,5.8)





















