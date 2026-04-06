class Animal:
    def sound(self):
        print("Якийсь звук")

class Dog(Animal):
    def sound(self):
        print("Гав-гав")

class Cat(Animal):
    def sound(self):
        print("Мяу")

class Cow(Animal):
    def sound(self):
        print("Му")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
    
#У Python використовується пізнє зв’язування (динамічна диспетчеризація), 
# що означає, що вибір методу відбувається під час виконання програми залежно
# від типу об’єкта, а не під час написання коду.