# ЗАДАНИЕ 2 с использованием полиморфизма:
# Продемонстрировать принцип полиморфизма через реализацию разных классов, представляющих
# геометрические формы, и метод для расчёта площади каждой формы.
# 1. Создать базовый класс Shape с методом area(), который просто возвращает 0.
# 2. Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square),
#    каждый из которых переопределяет метод area().
# 3. В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# 4. Написать функцию, которая принимает объект класса Shape и выводит его площадь.

class Shape():
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2 # Возвращаем площадь круга

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Возвращаем площадь прямоугольника

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2  # Возвращаем площадь квадрата


def print_area(shape): # shape — фигура (объект класса), которая будет использоваться
    print(f"Площадь фигуры - {shape.area()}")

circle = Circle(5)
print_area(circle)

rectangle = Rectangle(7, 6)
print_area(rectangle)

square = Square(7)
print_area(square)
