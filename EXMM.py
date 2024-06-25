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


def print_functions():
    print("Доступные функции:")
    print("1. Crypter")
    print("2. Portpars")
    print("3. Textcur")
    print("4. Datgen")
    print("5. Network info")
    print("6. Hash calculator")
    print("7. Usergen")
    print("8. Base64conv")
    print("9. Dominpars")
    print("10. Qrgen")
    print("11. Metapars")
    print("12. System info")
    print("13. Passgen")
    print("14. Emailgen")
    print("15. Phonepars")

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
    clear()
    print(Colorate.Horizontal(Colors.cyan_to_green, logo))

    Anime.Fade(
        Center.XCenter(logo),
        Colors.cyan_to_green,
        Colorate.Vertical,
        enter=True
    )

def mainstart():
    clear_and_print_logo()
    print_functions()
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
            print("er")
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
            print("er")
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
    mainstart()