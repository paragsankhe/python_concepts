class MyClass:
    i, j = 10,20 #class variables

    def add(self):
        print(self.i + self.j) #30

mc = MyClass()
mc.add()