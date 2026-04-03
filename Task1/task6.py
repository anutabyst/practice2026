def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  

num = int(input("Введіть число для обчислення факторіала: "))

if num < 0:
    print("Факторіал визначений тільки для невід’ємних чисел")
else:
    result = factorial(num)
    print(f"Факторіал числа {num} = {result}")