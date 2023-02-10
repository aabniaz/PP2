class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        Shape.__init__(self)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

area_of_rectangle = Rectangle(int(input()), int(input()))
print(area_of_rectangle.area())            #with given input
print(Rectangle().area())                  #default area = 0




