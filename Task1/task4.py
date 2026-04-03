import math

v0 = float(input("Введіть початкову швидкість (м/с): "))
theta_deg = float(input("Введіть кут вильоту (градуси): "))

theta = math.radians(theta_deg)

g = 9.8  

vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)

H_max = (vy**2) / (2 * g)
print(f"Максимальна висота: {H_max:.2f} м")

t_flight = 2 * vy / g
print(f"Час польоту: {t_flight:.2f} с")


print("\nВисота снаряда на кожну секунду:")
t = 0
while t <= t_flight:
    y = vy * t - 0.5 * g * t**2
    print(f"t = {t:.0f} с: y = {y:.2f} м")
    t += 1

range_x = vx * t_flight
print(f"\nДальність польоту: {range_x:.2f} м")