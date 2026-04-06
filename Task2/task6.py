class Animal:
    def sound(self):
        print("Тварина видає звук")

class Dog(Animal):
    def sound(self):
        print("Гав-гав")

class Cat(Animal):
    def sound(self):
        print("Мяу")

class Cow(Animal):
    def sound(self):
        print("Му")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()