from abcd import ABC, abstractmethod

class X(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

class Y(X):
    def method1(self):
        print("we are inside method 1")

class Z(Y):
    def method2(self):
        print("we are inside method2")

myobj = Z()
myobj.method1()
myobj.method2()