class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand      
        self.year = year        
        self.mileage = mileage 

    def drive(self, km):
        self.mileage += km
        print(f"Авто {self.brand} проїхало ще {km} км. Загальний пробіг: {self.mileage} км.")

    def info(self):
        print(f"Марка: {self.brand}, Рік випуску: {self.year}, Пробіг: {self.mileage} км")

    def __str__(self):
        return f"{self.brand} ({self.year}) — пробіг: {self.mileage} км"