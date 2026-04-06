class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def show_info(self):
        print(f"Студент: {self.name} | Група: {self.group} | Середній бал: {self.average_grade}")


students = [
    Student("Анна", "ІП-21", 90),
    Student("Олег", "ІП-22", 75),
    Student("Марія", "ІП-21", 88)
]

for student in students:
    student.show_info()