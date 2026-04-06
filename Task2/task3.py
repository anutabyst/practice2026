students = {}
all_grades = [] 

n = int(input("Скільки студентів? "))

for i in range(n):
    name = input("\nВведіть ім'я студента: ")

    grades_input = input("Введіть оцінки через пробіл: ")
    grades = list(map(int, grades_input.split()))

    all_grades.extend(grades)
    
    average = sum(grades) / len(grades)

    students[name] = average

unique_grades = set(all_grades)

print("\nСередній бал студентів:")
for name, avg in students.items():
    print(f"{name}: {avg:.2f}")

print("\nУнікальні оцінки:", unique_grades)