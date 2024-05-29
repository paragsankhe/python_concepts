
a,b = 10, 80 #global variables
class A:
    a,b = 20, 30 #class variables

class B(A):
    a,b = 50,60 #class variables
    def add(self,a,b): #local variables
        print(a+b) #12
        print(self.a+self.b) #110
        print(super().a + super().b) #50
        print(globals()['a'] + globals()['b']) #90

myobjb = B()
myobjb.add(7,5)