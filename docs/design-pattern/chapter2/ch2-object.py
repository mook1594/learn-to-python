import math

class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2)


p1 = Point(3, 5)
p2 = Point()

print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1.calculate_distance(p2))

# p1.reset(p2)
# print(p1.x, p1.y)
