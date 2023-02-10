class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return self.length ** 2

area_of_square = Square(int(input()))
print(area_of_square.area())            #with given input
print(Square().area())                  #default area = 0




