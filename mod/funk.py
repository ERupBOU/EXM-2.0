#all funk

import re
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import random
import string
import platform
import psutil
import shutil
import socket
import netifaces
import requests
import pyudev
import shutil
import os
import exifread
import mutagen
import PyPDF2



























#========================================
def metapars():
    image_path = input("[?] Путь к файлу > ")
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
        metadata = {}
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'EXIF MakerNote'):
                metadata[tag] = tags[tag]
    return metadata
#========================================
def systempars():
    print("System Information:")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"CPU: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")

    print("\nCPU Information:")
    print(f"CPU Count: {psutil.cpu_count()}")
    print(f"CPU Utilization: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz")

    print("\nMemory Information:")
    mem = psutil.virtual_memory()
    print(f"Total Memory: {round(mem.total / (1024.0 ** 3), 2)} GB")
    print(f"Available Memory: {round(mem.available / (1024.0 ** 3), 2)} GB")
    print(f"Used Memory: {round(mem.used / (1024.0 ** 3), 2)} GB")
    print(f"Memory Usage: {mem.percent}%")

    print("\nDisk Information:")
    disk = shutil.disk_usage("/")
    print(f"Total Disk Space: {round(disk.total / (1024.0 ** 3), 2)} GB")
    print(f"Used Disk Space: {round(disk.used / (1024.0 ** 3), 2)} GB")
    print(f"Free Disk Space: {round(disk.free / (1024.0 ** 3), 2)} GB")
    print(f"Disk Usage: {round(disk.used / disk.total * 100, 2)}%")

    print("\nNetwork Information:")
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {round(net_io.bytes_sent / (1024.0 ** 2), 2)} MB")
    print(f"Bytes Received: {round(net_io.bytes_recv / (1024.0 ** 2), 2)} MB")

    print("\nNetwork Interfaces:")
    for interface in netifaces.interfaces():
        print(f"Interface: {interface}")
        try:
            addr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
            print(f"IP Address: {addr}")
        except (ValueError, IndexError):
            print("IP Address: N/A")
        try:
            netmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
            print(f"Netmask: {netmask}")
        except (ValueError, IndexError):
            print("Netmask: N/A")
        try:
            broadcast = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['broadcast']
            print(f"Broadcast: {broadcast}")
        except (ValueError, IndexError):
            print("Broadcast: N/A")
        print()

    print("\nConnected Devices:")
    context = pyudev.Context()
    for device in context.list_devices(subsystem='input'):
        if 'ID_INPUT_KEYBOARD' in device.properties:
            print(f"Keyboard: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_MOUSE' in device.properties:
            print(f"Mouse: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_TOUCHPAD' in device.properties:
            print(f"Touchpad: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_TOUCHSCREEN' in device.properties:
            print(f"Touchscreen: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_TABLET' in device.properties:
            print(f"Tablet: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_JOYSTICK' in device.properties:
            print(f"Joystick: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_VIDEO_DISPLAY' in device.properties:
            print(f"Monitor: {device.get('ID_MODEL')}")

    print("\nDisplay Information:")
    try:
        edid = os.popen('get-edid').read()
        edid_lines = edid.split('\n')
        for line in edid_lines:
            if line.startswith('Manufacturer:'):
                print(f"Manufacturer: {line.split(':')[1].strip()}")
            elif line.startswith('Monitor Name:'):
                print(f"Model: {line.split(':')[1].strip()}")
            elif line.startswith('Detailed Timing Description:'):
                width, height = line.split(',')[0].split()[1].split('x')
                refresh_rate = line.split(',')[1].strip().split()[0]
                print(f"Resolution: {width}x{height}")
                print(f"Refresh Rate: {refresh_rate} Hz")
    except:
        print("Unable to retrieve display information.")

    print("\nOther Information:")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Public IP Address: {requests.get('https://api.ipify.org').text}")
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