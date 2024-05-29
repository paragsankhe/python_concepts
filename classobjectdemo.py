class MyClass:
    def printname(self):
        print("inside printname method")
    def printemail(self, email, empid):
        print("email is", email, empid)

p1 = MyClass()
p1.printname()
p1.printemail("test@gmail.com", 100)

p2 = MyClass()
p2.printname()
p2.printemail("test2@gmail.com", 101)