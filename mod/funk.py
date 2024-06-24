import re
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import random
import string
import platform
import shutil
import socket
import requests
import pyudev
import os
import exifread
import mutagen
import PyPDF2
import qrcode
import base64
import hashlib
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import tldextract





#========================================
def crypter():
    file_path = input("Введите путь к файлу: ")
    mode = input("Введите режим работы (encrypt/decrypt): ")
    key = get_random_bytes(16)
    
    block_size = 16
    cipher = AES.new(key, AES.MODE_ECB)
    
    with open(file_path, 'rb') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            if mode == 'encrypt':
                encrypted_block = cipher.encrypt(block)
            elif mode == 'decrypt':
                encrypted_block = cipher.decrypt(block)
            else:
                raise ValueError("Неверный режим работы функции.")
            with open(f"{file_path}.{'encrypted' if mode == 'encrypt' else 'decrypted'}", 'ab') as output_file:
                output_file.write(encrypted_block)
    
    if mode == 'encrypt':
        print(f"Файл {file_path}.encrypted успешно зашифрован.")
    else:
        print(f"Файл {file_path}.decrypted успешно расшифрован.")

#========================================
def textcur():
    custom_map = {
        'а': '@', 'б': 'Б', 'в': 'B', 'г': 'г', 'д': 'д', 'е': 'е', 'ё': 'ё', 'ж': 'ж',
        'з': '3', 'и': 'u', 'й': 'й', 'к': 'K', 'л': 'л', 'м': 'M', 'н': 'H', 'о': '0',
        'п': 'п', 'р': 'P', 'с': 'c', 'т': 'T', 'у': 'y', 'ф': 'ф', 'х': 'X', 'ц': 'ц',
        'ч': '4', 'ш': 'ш', 'щ': 'щ', 'ъ': 'ъ', 'ы': 'ы', 'ь': 'ь', 'э': 'э', 'ю': 'ю',
        'я': 'я', 'А': 'A', 'Б': '6', 'В': 'V', 'Г': 'r', 'Д': 'D', 'Е': 'E', 'Ё': 'Ё',
        'Ж': 'Ж', 'З': '2', 'И': 'I', 'Й': 'Й', 'К': 'K', 'Л': 'Л', 'М': 'M', 'Н': 'H',
        'О': 'O', 'П': 'П', 'Р': 'P', 'С': 'C', 'Т': 'T', 'У': 'Y', 'Ф': 'Ф', 'Х': 'X',
        'Ц': 'Ц', 'Ч': 'Ч', 'Ш': 'Ш', 'Щ': 'Щ', 'Ъ': 'Ъ', 'Ы': 'bl', 'Ь': 'b', 'Э': 'Э',
        'Ю': '9Y', 'Я': '9A'
    }

    user_text = input("Введите текст: ")
    replaced_text = ''
    for char in user_text:
        if char.lower() in custom_map:
            replaced_text += custom_map[char.lower()]
        else:
            replaced_text += char
    print("Текст с замененными буквами:", replaced_text)

#======================================
def portpars():
    host = input("Введите хост для сканирования: ")
    
    start_port = int(input("Введите начальный порт: "))
    end_port = int(input("Введите конечный порт: "))
    
    print(f"Сканирование хоста {host} в диапазоне портов от {start_port} до {end_port}...")
    
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((host, port))
            
            if result == 0:
                print(f"Порт {port} открыт")
            sock.close()
    except socket.gaierror:
        print(f"Ошибка: Не удалось разрешить хост {host}")
    except socket.error:
        print(f"Ошибка: Не удалось установить соединение с хостом {host}")
#========================================
def netpars():
    print("Сетевая информация:")
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        print(f"Интерфейс: {iface}")
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            for link in addrs[netifaces.AF_INET]:
                print(f"  IP-адрес: {link['addr']}")
                print(f"  Маска подсети: {link['netmask']}")
        if netifaces.AF_LINK in addrs:
            for link in addrs[netifaces.AF_LINK]:
                print(f"  MAC-адрес: {link['addr']}")
        print()
 
#========================================
def datgen():
    num_dates = int(input("Введите количество дат, которое нужно сгенерировать: "))
    dates = generate_random_dates(num_dates)
    for date in dates:
        print(f"Формат ГГГГ-ММ-ДД: {date[0]}")
        print(f"Формат ДД.ММ.ГГГГ: {date[1]}")
        print()

def generate_random_dates(num_dates):
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2023, 12, 31)

    dates = []
    for _ in range(num_dates):
        random_date = start_date + timedelta(seconds=random.randint(0, (end_date - start_date).total_seconds()))
        dates.append((random_date.strftime("%Y-%m-%d"), random_date.strftime("%d.%m.%Y")))

    return dates

#=======================================
def genuser():
    num_user_agents = int(input("Введите количество user agent строк, которые нужно сгенерировать: "))
    for _ in range(num_user_agents):
        platform = random.choice(['Windows', 'Macintosh', 'Linux', 'iPhone', 'Android'])
        browser = random.choice(['Chrome', 'Firefox', 'Safari', 'Opera', 'Edge'])
        version = ''.join(random.choices(string.digits, k=2)) + '.' + ''.join(random.choices(string.digits, k=1)) + '.' + ''.join(random.choices(string.digits, k=1))
        user_agent = f"Mozilla/5.0 ({platform}; rv:{version}) Gecko/20100101 {browser}/{version}"
        print(user_agent)
#=======================================
def hash_calculator(input_text, hash_type):
    if hash_type == 'md5':
        return hashlib.md5(input_text.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(input_text.encode()).hexdigest()
    else:
        raise ValueError("Недопустимый тип хеша. Используйте 'md5' или 'sha256'.")

if __name__ == "__main__":
    user_input = input("Введите текст для вычисления хеша: ")
    hash_type = input("Введите тип хеша (md5 или sha256): ")
    
    try:
        computed_hash = hash_calculator(user_input, hash_type)
        print(f"{hash_type.upper()} хеш: {computed_hash}")
    except ValueError as e:
        print(e)
#=======================================
def domainpars():
    domain = input("Введите домен: ")
    extract = tldextract.extract(f"http://{domain}")
    
    print(f"Найден домен: {domain}")
    print(f"Публичный суффикс: {extract.suffix}")
    print(f"Субдомен: {extract.subdomain}")
    print(f"Основной домен: {extract.domain}")

#========================================
def base64conv():
    choice = input("Выберите операцию (1 - Кодировать, 2 - Декодировать): ")

    if choice == "1":
        text = input("Введите текст для кодирования в base64: ")
        encoded_text = base64.b64encode(text.encode()).decode()
        print(f"Закодированный текст: {encoded_text}")
    elif choice == "2":
        b64_text = input("Введите текст, закодированный в base64: ")
        decoded_text = base64.b64decode(b64_text.encode()).decode()
        print(f"Декодированный текст: {decoded_text}")
    else:
        print("Неверный выбор. Попробуйте еще раз.")
        base64_converter()
#========================================


def qrgen():
    url = input("Введите ссылку: ")
    save_path = input("Введите путь для сохранения QR-кода (например, 'C:/Users/username/qrcode.png'): ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)
    print(f"QR-код успешно создан и сохранен в файле '{save_path}'.")
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
def passgen():
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
                print("[!] Вы должны выбрать хотя бы один тип символов.")
                continue

            password = ''.join(random.choice(characters) for i in range(length))
            print("Сгенерированный пароль:", password)

            choice = input("[?] Хотите сгенерировать другой пароль? (y/n) ")
            if choice.lower() == "n":
                print("[*] Возвращение в главное меню...")
                break
            elif choice.lower() == "y":
                continue
            else:
                print("[!] Неверный выбор. Пожалуйста, попробуйте еще раз.")

        except ValueError:
            print("[!] Недопустимый ввод. Пожалуйста, введите положительное целое число для длины пароля.")
            continue
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