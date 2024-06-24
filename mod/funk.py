#all funk

import re
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import random
import string



















#========================================
def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    try:
        characters = ""
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            return None

        password = ''.join(random.choice(characters) for i in range(length))
        return password
    except ValueError:
        return None

def get_password_options():
    while True:
        try:
            length = int(input("Введите длину пароля: "))
            if length <= 0:
                print("[!] Длина пароля должна быть положительным целым числом.")
                continue

            use_lowercase = input("Использовать строчные буквы? (да/нет) ").lower() == "да"
            use_uppercase = input("Использовать прописные буквы? (да/нет) ").lower() == "да"
            use_digits = input("Использовать цифры? (да/нет) ").lower() == "да"
            use_special = input("Использовать специальные символы? (да/нет) ").lower() == "да"

            return length, use_lowercase, use_uppercase, use_digits, use_special
        except ValueError:
            print("[!] Недопустимый ввод. Пожалуйста, введите положительное целое число для длины пароля.")
            continue

def run_password_generator():
    while True:
        length, use_lowercase, use_uppercase, use_digits, use_special = get_password_options()
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
        if password is None:
            print("[!] Не удалось сгенерировать пароль. Пожалуйста, попробуйте еще раз.")
        else:
            print("Сгенерированный пароль:", password)

        choice = input("[?] Хотите сгенерировать другой пароль? (y/n) ")
        if choice.lower() == "n":
            print("[*] Возвращение в главное меню...")
            break
        elif choice.lower() == "y":
            continue
        else:
            print("[!] Неверный выбор. Пожалуйста, попробуйте еще раз.")
#========================================
def emailGen():
    first_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    last_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))

    username = f"{first_name.lower()}.{last_name.lower()}"
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 5)))
    email = f"{username}{random_chars}@example.com"

    password_length = random.randint(8, 16)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

    print(f"Сгенерированный email: {email}")
    print(f"Сгенерированный пароль: {password}")

emailGen()
#========================================
def phonepars():
    while True:
        phone_number = input("Введите номер телефона (например, +79991234567): ")
        try:
            parsed_number = phonenumbers.parse(phone_number)
            if not phonenumbers.is_valid_number(parsed_number):
                print("Некорректный номер телефона. Попробуйте еще раз.")
                continue
            
            country = geocoder.description_for_number(parsed_number, "ru")
            provider = carrier.name_for_number(parsed_number, "ru")
            timezone_info = timezone.time_zones_for_number(parsed_number)
            country_code = parsed_number.country_code
            national_number = parsed_number.national_number
            is_mobile = "мобильный" if phonenumbers.is_mobile_number(parsed_number) else "стационарный"
            
            phone_info = [
                f"Страна: {country}",
                f"Код страны: +{country_code}",
                f"Номер: {national_number}",
                f"Тип: {is_mobile}",
                f"Провайдер: {provider}",
                f"Часовой пояс: {', '.join(timezone_info)}"
            ]
            print("\n".join(phone_info))
            break
        except (phonenumbers.phonenumberutil.NumberParseException, IndexError):
            print("Некорректный формат номера телефона. Попробуйте еще раз.")