import math 

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

if a == 0:
    print("Це не квадратне рівняння (a не може бути 0)")
else:
    D = b**2 - 4*a*c
    print("Дискримінант D =", D)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Два дійсних корені: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2*a)
        print(f"Один дійсний корінь: x = {x}")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*a)
        print(f"Два комплексні корені: x1 = {real_part}+{imaginary_part}i, x2 = {real_part}-{imaginary_part}i")