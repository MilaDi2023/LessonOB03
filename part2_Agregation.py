# Пример кода с использованием ассоциации между классами типа АГРЕГАЦИЯ

class Teacher():
    def teach(self):
        print("Преподаватель нас учит")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        print("Урок начался")
        self.teacher.teach()

    def stop_lesson(self):
        print("Урок окончен")

# При использовании АГРЕГАЦИИ объект создаётся не внутри зависимого класса, а ЗА его пределами
my_teacher = Teacher()

# Создаем отдельно объект класса my_school и передадим туда my_teacher
my_school = School(my_teacher)

# Отработка кода
my_school.start_lesson()
my_school.stop_lesson()