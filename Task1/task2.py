DIGITS = "0123456789"

number = int(input("Введіть число: "))
output = ""

if number == 0:
    output = "0"

is_negative = number < 0
if is_negative:
    number = -number

while number > 0:
    digit = number % 10          
    output = DIGITS[digit] + output  # додаємо спереду
    number = number // 10        # видаляємо останню цифру

# додаємо знак мінус, якщо потрібно
if is_negative:
    output = "-" + output

print("Рядок:", output)