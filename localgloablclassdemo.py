# local , class and global variables

# i,j = 30,40 #global varibales
# class MyClass:
#     x, y = 10,20 #class variables
#
#     def add(self,a,b): #local variables
#         print(a + b)   #11
#         print(self.x + self.y) #30
#         print(i + j) #70
#
# mc = MyClass()
# mc.add(5,6)

# when local , class and global varibales have the same name

a, b = 30, 40
class MyClass:
    a, b = 100, 200

    def add(self,a, b):
        print(a + b) #15
        print(self.a + self.b) #300
        print(globals()["a"] +globals()["b"]) #70

mc = MyClass()
mc.add(5,10)

















