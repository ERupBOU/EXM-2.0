from mod.funk import *


import os
import platform
import time
from pystyle import Colorate, Colors, Anime, Center


def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux' or system == 'Darwin':
        os.system('clear')



def printfunk():
    print('''
 1 Шифровальщик файлов
 2 Сканер портов 
 3 Искажатель текста 
 4 Генератор дат 
 5 Сетевая информация
 6 Калькулятор хеша 
 7 Генератор юзеров
 8 Кодер/декодер base64
 9 Информация о домене
10 Генератор qr-кодов
11 Метаданные изображения
12 Информация системы
12 Генератор паролей
13 Генератор почт
14 Информация о номере
''')





logo = '''
                                      
▀███▀▀▀███▀███▀   ▀██▀▀████▄     ▄███▀
  ██    ▀█  ███▄  ▄█    ████    ████  
  ██   █     ▀██▄█▀     █ ██   ▄█ ██  
  ██████       ███      █  ██  █▀ ██  
  ██   █  ▄  ▄█▀▀██▄    █  ██▄█▀  ██  
  ██     ▄█ ▄█   ▀██▄   █  ▀██▀   ██  
▄████████████▄▄  ▄▄███▄███▄ ▀▀  ▄████▄
  
soft by EXM TG:ZBYKCMEPTU                                    
                                      

'''

def clear_and_print_logo():
   cleer()
   while True:
       print(Colorate.Horizontal(Colors.cyan_to_green, logo))
    Anime.Fade(
        Center.XCenter(logo),
        Colors.cyan_to_green,
        Colorate.Vertical,
        enter=True
    )






def mainstart():
    clear_and_print_logo()
    printfunk()
    while True:
    choice = int(input("[?]>>"))
    if choice == 1:
        clear_and_print_logo()
        crypter()
    elif choice == 2:
        clear_and_print_logo()
        portpars()
    elif choice == 3:
        clear_and_print_logo()
        textcur()
    elif choice == 4:
        clear_and_print_logo()
        datgen()
    elif choice == 5:
        clear_and_print_logo()
        netpars()
    elif choice == 6:
        clear_and_print_logo()
        hash_calculator()
    elif choice == 7:
        clear_and_print_logo()
        usergen()
    elif choice == 8:
        clear_and_print_logo()
        base64conv()
    elif choice == 9:
        clear_and_print_logo()
        dominpars()
    elif choice == 10:
        clear_and_print_logo()
        qrgen()
    elif choice == 11:
        clear_and_print_logo()
        metapars()
    elif choice == 12:
        clear_and_print_logo()
        syspars()
    elif choice == 13:
        clear_and_print_logo()
        passgen()
    elif choice == 14:
        clear_and_print_logo()
        emailgen()
    elif choice == 15:
        clear_and_print_logo()
        phonepars()  
    elif choice == 33:
        break
    else:
        print("[¿]>>")
        continue


if __name__ == "__main__":
    while True:
        mainstart()

