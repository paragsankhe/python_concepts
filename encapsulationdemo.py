class Employee:
    empname = "Jack"
    __salary = 5000

    def getsalary(self):
        print("salary is", self.__salary)

    def setsalary(self,salary):
        if (salary < 5000 or salary>10000):
            print("salary is not in range")
        else:
            self.__salary = salary


emp1 = Employee()
print(emp1.empname)
emp1.setsalary(7000)
emp1.getsalary()
