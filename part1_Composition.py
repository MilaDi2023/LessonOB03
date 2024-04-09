# Пример кода с использованием ассоциации между классами типа КОМПОЗИЦИЯ

class Engine(): # Создаём основной класс Engine
    def start(self):
        print("Двигатель включён")

    def stop(self):
        print("Двигатель остановлен")

class Car(): # Создаём класс Car, который жёстко связан с классом Engine. Пропадёт Engine, и Car не сможет работать
    def __init__(self):
        self.engine = Engine() # Зависимость от Engine

    def start(self):
        self.engine.start() # Зависимость от Engine

    def stop(self):
        self.engine.stop() # Зависимость от Engine

# Созадём объекты класса
my_Car = Car()

# Запускаем работу класса Car. Он работает на функциях из класса Engine
my_Car.start()
my_Car.stop()