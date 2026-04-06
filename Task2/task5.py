class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Поповнення на {amount}. Баланс: {self.__balance}")
        else:
            print("Сума має бути більше 0")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостатньо коштів!")
        elif amount <= 0:
            print("Сума має бути більше 0")
        else:
            self.__balance -= amount
            print(f"Знято {amount}. Баланс: {self.__balance}")

    def get_balance(self):
        return self.__balance