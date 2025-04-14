from faker import Faker
import random
import string

# Переменная для библиотеки Faker
fake = Faker(['ru_RU'])

# Функция для генерации пароля
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

# Функция для генерации данных пользователя
def generate_user_data():
    email = fake.email()
    password = generate_random_string(12)
    name = fake.name()
    return email, password, name