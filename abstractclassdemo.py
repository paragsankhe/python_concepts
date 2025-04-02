from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod
    def color(self):
        pass

class Mango(Fruit):
    def color(self):
        print("mango is having yellow color")

class Cherry(Fruit):
    def color(self):
        print("cherry is red colored")

obj1 = Mango()
obj1.color()

obj2 = Cherry()
obj2.color()

