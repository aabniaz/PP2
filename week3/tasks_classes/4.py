class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def show(self):
        print((self.x, self.y))

    def move(self, x = 0, y = 0):
        self.x += x
        self.y += y
        self.show()

    def dist(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

p = Point(2, 5)
p2 = Point(1, 3)
p.show()
p.move(x = 2, y = -2)
print(p.dist(p2.x, p2.y))