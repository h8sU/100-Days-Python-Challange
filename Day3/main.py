# Day 3: Spėk skaičių 

# Kompiuteris atsitiktinai pasirenka skaičių nuo 1 iki 100.
# Vartotojas spėja, kol atspėja teisingai.
# Po kiekvieno spėjimo pateikiama užuomina: "Per mažas", "Per didelis" arba "Teisingai".
# Galiausiai parodomas bandymų skaičius.

import random  # Įkeliame 'random' modulį, kuris leidžia generuoti atsitiktinius skaičius

slaptas_skaicius = random.randint(1, 100)  # Sugeneruojamas atsitiktinis slaptas skaičius nuo 1 iki 100

bandymai = 0  # Kintamasis, saugantis spėjimų skaičių

# Ciklas, kuris kartosis tol, kol vartotojas atspės skaičių
while True:
    try:
        spejimas = int(input("Tavo spėjimas: "))  # Paprašoma vartotojo įvesti skaičių ir konvertuojama į sveikąjį skaičių
        bandymai += 1  # Pridedamas vienas bandymas

        if spejimas > slaptas_skaicius:
            print("Per didelis")  # Spėjimas per didelis
        elif spejimas < slaptas_skaicius:
            print("Per mažas!")  # Spėjimas per mažas
        else:
            print(f"Teisingai! Slaptas skaičius buvo: {slaptas_skaicius}")  # Teisingas atsakymas
            print(f"Atspėjai per {bandymai} bandymų.")  # Parodomas bandymų skaičius
            break  # Išeinama iš ciklo

    except ValueError:
        print("Klaida! Įvesk tik sveikąjį skaičių.")  # Pranešama apie neteisingą įvestį
