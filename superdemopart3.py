class A:
    def __init__(self):
        print("Class A constructor invoked")

class B(A):
    def __init__(self):
        print("Class B constructor invoked")
        #super().__init__() #approach 1
        A.__init__(self) #Approch 2

myobjb = B()