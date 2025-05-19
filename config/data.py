import random
import string


# Генерация данных email и пароля
class GenerateData:
    def generate_email(self, domain="yandex.ru"):
        # Генерация случайного имени пользователя
        username_length = random.randint(5, 10)
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
        email = f"{username}@{domain}"
        return email

    def generate_password(self, length=12):
        # Генерация случайного пароля
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        return password


# Генерация названия продукта
class GenerateProductName:
    def generate_product_name():
        # Генерация случайного названия продукта
        product_name = f'Машинка {random.randint(100, 999)}'
        return product_name

    # Генерация имени продукта
PRODUCT_NAME = GenerateProductName.generate_product_name()