# ДОМАШНЕЕ ЗАДАНИЕ:
# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые
# наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает
# список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных
# и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке
# в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, cage):
        self.name = name
        self.cage = cage

    def animal_info(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, cage, color, voice):
        super().__init__(name, cage)
        self.color = color
        self.voice = voice
    def animal_info(self):
        print(f'В клетке №{self.cage} находится {self.name}, у него {self.color} окрас, а поёт он так: "{self.voice}"')

class Mammal(Animal):
    def __init__(self, name, cage, color, voice):
        super().__init__(name, cage)
        self.color = color
        self.voice = voice
    def animal_info(self):
        print(f'В вольере №{self.cage} живёт {self.name}, у него {self.color} окрас, и он издаёт звук "{self.voice}"')

class Reptile(Animal):
    def __init__(self, name, cage, color, voice):
        super().__init__(name, cage)
        self.color = color
        self.voice = voice
    def animal_info(self):
        print(f'В террариуме №{self.cage} обитают {self.name}, у которых {self.color} окрас. Обычно они молчат, но могут шипеть так: "{self.voice}"')


bird = Bird("голубь", "1", "сизый", "курлык-курлык")
mammal = Mammal("тигр", "2", "полосатый", "р-р-р-ряу!")
reptile = Reptile("аспиды", "3", "чёрный", "ш-ш-сссс...")

animals = [bird, mammal, reptile]

print(f"\n1. ИНФОРМАЦИЯ ОБ ОБИТАТЕЛЯХ ЗООПАРКА: (реализация полиморфизма классов Animal и Bird/Mammal/Reptile)")
print("==============================================================================================================")
for animal in animals:
    animal.animal_info()
print("==============================================================================================================")

class ZooKeeper:
    def __init__(self, name, animal, title):
        self.name = name
        self.animal = animal
        self.title = title

    def care_animal(self):
        if isinstance(self.animal, Bird):
            print(f'{self.title} {self.name} ухаживает за клеткой №{self.animal.cage}, в которой обитает {self.animal.name}')
        elif isinstance(self.animal, Mammal):
            print(f'Фелинолог {self.name} отвечает за вольером №{self.animal.cage}, где живёт {self.animal.name}')
        elif isinstance(self.animal, Reptile):
            print(f'Герпетолог {self.name} ответственен за террариум №{self.animal.cage}, где обитают {self.animal.name}')


ornithologist = ZooKeeper("Иван", bird, "Орнитолог")
felinologist = ZooKeeper("Петр", mammal, "Фелинолог")
herpetologist = ZooKeeper("Сергей", reptile, "Герпетолог")

keepers = [ornithologist, felinologist, herpetologist]

print(f"\n2. РАБОТНИКИ, УХАЖИВАЮЩИЕ ЗА ЖИВОТНЫМИ: (реализация композиции классов ZooKeeper и Bird/Mammal/Reptile)")
print("====================================================================================================")
for keeper in keepers:
    keeper.care_animal()
print("====================================================================================================")

class ZooWorker:
    def __init__(self, name, title, work):
        self.name = name
        self.title = title
        self.work = work

    def zoo_work(self):
        print(f"{self.title} {self.name}. Его обязанность - {self.work}")

veterinarian = ZooWorker("Степан", "Ветеринар", "быть доктором Айболитом для жителей зоопарка")
cooker = ZooWorker("Максим", "Повар", "готовить вкусную и полезную еду для зверей")
cleaner = ZooWorker("Джамшуд", "Уборщик", "содержать территорию зоопарка в идеальной чистоте")

workers = [veterinarian, cooker, cleaner]

print(f"\n3. ДРУГИЕ РАБОТНИКИ ЗООПАРКА: (это просто самоcтоятельный класс ZooWorker)")
print("======================================================================================")
for worker in workers:
    worker.zoo_work()
print("======================================================================================")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def get_employee_info_zookeeper(self, zookeeper):
        return f"{zookeeper.name}, {zookeeper.title}"

    def get_employee_info_worker(self, worker):
        return f"{worker.name}, {worker.title}"

    def get_animal_name(self, animal):
        return f"{animal.name}"

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_all_animals_info(self):
        print("\n4. СПИСОК ВСЕХ ЖИВОТНЫХ ЗООПАРКА:")
        print("*Используется метод класса Zoo, у которого композиция с классом Animal.*")
        print("========================================================================")
        for animal in self.animals:
            print(self.get_animal_name(animal))
        print("========================================================================")

    def print_all_employees_info(self):
        print("\n5. СПИСОК ВСЕХ РАБОТНИКОВ ЗООПАРКА:")
        print("*Используется метод класса Zoo, у которого композиция с классами ZooKeeper и ZooWorker.*")
        print("=========================================================================================")
        for employee in self.employees:
            if isinstance(employee, ZooKeeper):
                print(self.get_employee_info_zookeeper(employee))
            else:
                print(self.get_employee_info_worker(employee))


my_zoo = Zoo()

my_zoo.add_animal(bird)
my_zoo.add_animal(mammal)
my_zoo.add_animal(reptile)

my_zoo.add_employee(ornithologist)
my_zoo.add_employee(felinologist)
my_zoo.add_employee(herpetologist)
my_zoo.add_employee(veterinarian)
my_zoo.add_employee(cooker)
my_zoo.add_employee(cleaner)

my_zoo.print_all_animals_info()
my_zoo.print_all_employees_info()