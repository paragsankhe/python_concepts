# class Shape:
#     myvar = "shapeparent"
#
# class Circle(Shape):
#     myvar = "Circleshape"
#
# cirobj = Circle()
# print(cirobj.myvar)

#method overriding

class Shape():
    def draw(self):
        print("this is generic draw method in parent class")

class Circle(Shape):
    def draw(self):
        print("this is circle draw method")

class Rectangle(Shape):
    def draw(self):
        print("this is Rectangle draw method")

class Square(Shape):
    def draw(self):
        print("this is Square draw method")

cirobj = Circle()
cirobj.draw()
recobj = Rectangle()
recobj.draw()

shapeobj = Shape()
shapeobj.draw()

















