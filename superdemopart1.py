class A:
    def m2(self):
        print("we are inside method m2 of class A")

class B(A):
    def m1(self):
        print("we are inside method m1 of class B")
        super().m2()

myobjb = B()
myobjb.m1()


