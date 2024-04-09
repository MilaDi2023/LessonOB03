# ЗАДАНИЕ 1 с использованием полиморфизма:
# Создайте класс Animal с методом make_sound().
# Затем создайте несколько дочерних классов (например, Dog, Cat, Cow),
# которые наследуют Animal, но изменяют его поведение (метод make_sound()).
# В конце создайте список содержащий экземпляры этих животных и
# вызовите make_sound() для каждого животного в цикле.

# Создаём базовый класс
class Animal():
    def make_sound(self):
        pass

# Создаём 3 дочерних класса
class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу!")

class Cow(Animal):
    def make_sound(self):
        print("Му-у!")

# Создаём список из элементов каждого класса
animals = [Dog(), Cat(), Cow()]

# Запускаем цикл с использованием полиморфной функции make_sound
for animal in animals:
    animal.make_sound()