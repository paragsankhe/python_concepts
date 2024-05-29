# class A:
#     def mydisp1(self):
#         print("inside mydisp1 method")
#
#     def __mydisp2(self): #private method
#         print("inside mydisp2 method")
#
#     def mydisp3(self):
#         self.__mydisp2()
#
# myobj = A()
# myobj.mydisp1()
# myobj.mydisp3()

class A:
    myvar1 = 100 #public variable
    __myvar2 = 200 #private variable

    def display(self):
        print(self.__myvar2)

myobj = A()
print(myobj.myvar1)
myobj.display()















