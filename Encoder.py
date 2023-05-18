import random

class NumberEncryptor:
    def __init__(self, number):
        self.__number = number

    def __encrypt(self):
        self.__number += random.randint(1, 10)

    def decrypt(self):
        self.__encrypt()  # Виклик приватного методу для шифрування
        return self.__number

# Створюємо об'єкт-шифратор
encryptor = NumberEncryptor(42)

print(encryptor)
# Розшифровуємо та виводимо результат
result = encryptor.decrypt()
print(result)  # Виведе випадкове число, наприклад: 49
