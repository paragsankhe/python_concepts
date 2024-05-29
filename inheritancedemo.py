#Single inheritance

# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b = 40,30
#     def m2(self):
#         print(self.a - self.b)
#
# objb = B()
# print(objb.a) #40
# print(objb.b) #30
# objb.m2() #10
# objb.m1() #30
# print(objb.x) #10
# print(objb.y) #20

#Multilevel inheritance
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b = 40,30
#     def m2(self):
#         print(self.a - self.b)
#
# class C(B):
#     m,n = 50,60
#     def m3(self):
#         print(self.m * self.n)
#
# objb = B()
# print(objb.a) #40
# print(objb.b) #30
# print(objb.x) #10
# print(objb.y) #20
# objb.m1() #30
# objb.m2() #10
#
# objc = C()
# objc.m1()
# objc.m2()
# objc.m3()
# print(objc.a)
# print(objc.b)
# print(objc.m)
# print(objc.n)
# print(objc.x)
# print(objc.y)

#hierarchical inheritance

# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b = 40,30
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A):
#     m,n = 50,60
#     def m3(self):
#         print(self.m * self.n)
#
# objb = B()
# objb.m2() #10
# objb.m1() #30
#
# objc = C()
# objc.m3() #3000
# objc.m1() #30

# Multiple inheritance

class A:
    x,y = 10,20
    def m1(self):
        print(self.x + self.y)

class B:
    a,b = 40,30
    def m2(self):
        print(self.a - self.b)

class C(A,B):
    m,n = 50,60
    def m3(self):
        print(self.m * self.n)

objc = C()
print(objc.x, objc.y, objc.a, objc.b, objc.m, objc.n)
objc.m3() #3000
objc.m2() #10
objc.m1() #30



































