from mod import *

clear()
printlogo()
printfunk()


while True:
    choice = int(input("[?]>>"))
    if choice == 1:
        clear_and_print_logo()
        phonepars()
    elif choice == 2:
        clear_and_print_logo()
        ipparse()
    elif choice == 3:
        clear_and_print_logo()
        nikpars()
    elif choice == 4:
        clear_and_print_logo()
        websear()
    elif choice == 5:
        clear_and_print_logo()
        dbpars()
    elif choice == 6:
        clear_and_print_logo()
        dompars()
    elif choice == 7:
        clear_and_print_logo()
        proxyGen()
    elif choice == 8:
        clear_and_print_logo()
        emailGen()
    elif choice == 9:
        clear_and_print_logo()
        passGen()
    elif choice == 10:
        clear_and_print_logo()
        qrcodeGen()
    elif choice == 11:
        clear_and_print_logo()
        randNumGen()
    elif choice == 12:
        clear_and_print_logo()
        hashCalc()
    elif choice == 13:
        clear_and_print_logo()
        base64DecEnc()
    elif choice == 14:
        clear_and_print_logo()
        randStringGen()
    elif choice == 15:
        clear_and_print_logo()
        currencyConv()
    elif choice == 16:
        clear_and_print_logo()
        whoisLookup()
    elif choice == 17:
        clear_and_print_logo()
        ccardGen()
    elif choice == 18:
        clear_and_print_logo()
        macLookup()
    elif choice == 19:
        clear_and_print_logo()
        tempEmailGen()
    elif choice == 20:
        clear_and_print_logo()
        uaGen()
    elif choice == 21:
        clear_and_print_logo()
        sysInfo()
    elif choice == 22:
        clear_and_print_logo()
        tgParse()
    elif choice == 23:
        clear_and_print_logo()
        vkParse()
    elif choice == 24:
        clear_and_print_logo()
        ocParse()
    elif choice == 25:
        clear_and_print_logo()
        metaData()
    elif choice == 26:
        clear_and_print_logo()
        netData()
    elif choice == 27:
        clear_and_print_logo()
        randDateGen()
    elif choice == 28:
        clear_and_print_logo()
        portScan()
    elif choice == 29:
        clear_and_print_logo()
        ipsteal()
    elif choice == 30:
        clear_and_print_logo()
        cryptFiles()
    elif choice == 31:
        clear_and_print_logo()
        coordLookup()
    elif choice == 32:
        clear_and_print_logo()
        textDistort()
    elif choice == 33:
        break
    else:
        print("[¿]>>")
