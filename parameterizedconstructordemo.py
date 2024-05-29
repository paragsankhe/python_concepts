# class MyClass:
#     name = "John"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# myobj = MyClass("Jack")

class Employee:
    def __init__(self,empname,empid,empsal):
        self.empname = empname
        self.empid = empid
        self.empsal = empsal

    def display(self):
        print("employee name is :", self.empname)
        print("employee id is :", self.empid)
        print("employee salary is ", self.empsal)

emp1 = Employee("Jenny",1,1000)
emp1.display()

emp2 = Employee("Daisy",2,3000)
emp2.display()

emp3 = Employee("Sam",3,5000)
emp3.display()





























