class Employee:

    def __init__(self,empname,empid,empsal):
        self.empname = empname
        self.empid = empid
        self.empsal  = empsal

    def __str__(self):
        return(" empname is {} empid is {} empsal {}".format(self.empname, self.empid, self.empsal))

emp1 = Employee("jack", 1, 2000)
print(emp1)

emp2 = Employee("John", 2 , 3000)
print(emp2)