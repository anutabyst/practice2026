n = int(input("Введіть кількість студентів у групі: "))

students = []

for i in range(n):
    print(f"\nСтудент {i+1}:")
    first_name = input("Ім'я: ")
    last_name = input("Прізвище: ")
    
    grades = []
    for j in range(1, 6):
        grade = float(input(f"Оцінка з предмету {j}: "))
        grades.append(grade)
    
    student = {
        "ім'я": first_name,
        "прізвище": last_name,
        "оцінки": grades
    }
    students.append(student)

print("\nСередній бал кожного студента:")
print("{:<15} {:<15} {:<10}".format("Ім'я", "Прізвище", "Середній бал"))
for student in students:
    avg = sum(student["оцінки"]) / len(student["оцінки"])
    print("{:<15} {:<15} {:<10.2f}".format(student["ім'я"], student["прізвище"], avg))


subject_sums = [0] * 5  
for student in students:
    for i in range(5):
        subject_sums[i] += student["оцінки"][i]

subject_avgs = [subject_sums[i]/n for i in range(5)]
print("\nСередній бал групи по кожному предмету:")
for i, avg in enumerate(subject_avgs, 1):
    print(f"Предмет {i}: {avg:.2f}") 
    
    