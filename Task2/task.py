import math  

def rectangle_area(a, b):
    return a * b

def circle_area(r):
    return math.pi * r ** 2

print("Пряутник:")
a = float(input("Введіть довжину: "))
b = float(input("Введіть ширину: "))
print("Площа:", rectangle_area(a, b))

print("\nКоло:")
r = float(input("Введіть радіус: "))
print("Площа:", circle_area(r))



class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2



rect = Rectangle(5, 3)
circle = Circle(4)

print("Площа прямокутника:", rect.area())
print("Площа кола:", circle.area())