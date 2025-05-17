# Day 6: Monetos metimo simuliacija 
# Programa atsitiktinai parenka: „herbas“ arba „skaičius“


# Statistika kiek kartu iskrito kuri monetos puse
# mini animacija kada moneta sukasi..

# While 

# while True:
#    ivestis = input("Taip/Ne: ")
#
#    if ivestis.upper() == "NE":
#        break

# count - Skaiciuoja kiekvieno rezultato pasikartojimus

# clear_screen() - isvalyti terminal windows "cls"

# ANSI - kodus suteikti kodui spalvu atvaizduojant terminale

#input() - leidzia vartotojui ivesti ivesti.

### --- Kodas --- ###


import random # Atsitiktinis pasirinkimas
import time # animacijai suteiks laiko
import os # leidzia python kodui "bendrauti" su musu operacine sistema 

# Ekrona isvalymui
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Galimi variantai
sides = ['Herbas', 'Skaicius']

#Sukimosi animacijos 
spin_text = ['Sukasi...', 'Sukasi...', 'Sukasi...']

# Saitliukas - statistika
count = {"Herbas": 0, "Skaicius": 0}


while True:
    # Sukimosi animacija
    for _ in range(4):
        for text in spin_text:
            clear_screen()
            print(text)
            time.sleep(0.1)

    # Atsitiktinis rezultatas 
    result = random.choice(sides)
    count[result] += 1

    #Parodomas rezultatas su spalva
    GELTONA = "\033[93m"
    END = "\033[0m"

    print(GELTONA + f"Rezultatas: {result}" + END )

    # Rodoma statistika
    print(f" Statistikos suvestine")
    print(f"  Herbas: {count['Herbas']} kartus")
    print(f"  Skaicius: {count['Skaicius']} kartus")

    # Paklausima ar kartoti

    chouse = input("\n Mesti dar karta? (Taip/Ne): ").strip().upper()

    if chouse != "TAIP":
        clear_screen()
        print("Aciu, kad zaidiai!")
        break