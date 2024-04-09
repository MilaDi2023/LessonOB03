# Пример кода с применением ПОЛИМОРФИЗМА

class Dog:
    def speak(self):
        return "Гав-гав!"

class Cat:
    def speak(self):
        return "Мяу-мяу!"

def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

# Функция speak() имеется в обоих классах, но работает по-разному:
animal_speak(dog) # Выводит Гав-гав!
animal_speak(cat) # Выводит Мяу-мяу!