import random  # generování náhodných čísel
import os  # práce s cestami k souborům

def vyber_soubor(obtiznost):
    absolutni_cesta = r"C:\Users\olgah\Desktop\DataFiles"
    os.chdir(absolutni_cesta)
    if obtiznost == 1:
        file_name = "1.txt"
    elif obtiznost == 2:
        file_name = "2.txt"
    elif obtiznost == 3:
        file_name = "3.txt"
    else:
        print("Neplatná obtížnost.")
        return None

    file_path = os.path.join(absolutni_cesta, file_name)
    return file_path

def zobraz_prikaz(soubor):
    try:
        with open(soubor, 'r', encoding='utf-8') as file:
            prikazy = file.readlines()
            nahodny_prikaz = random.choice(prikazy)
            print("Náhodný příkaz:")
            print(nahodny_prikaz)
    except FileNotFoundError:
        print("Soubor nebyl nalezen.")

while True:
    obtiznost = int(input("Zvolte obtížnost (1, 2 nebo 3) nebo 0 pro ukončení: "))
    if obtiznost == 0:
        break
    soubor = vyber_soubor(obtiznost)
    if soubor:
        zobraz_prikaz(soubor)