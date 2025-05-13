#  Day 2: Paprasta CLI skaičiuoklė

# Užduotis:
# Sukurk programą, kuri veikia kaip skaičiuotuvas terminale.
# Vartotojas turi galėti pasirinkti veiksmą: +, -, *, /
# Įvedus du skaičius – programa paskaičiuoja ir atvaizduoja rezultatą.
# Įgyvendink galimybę tęsti skaičiavimus tol, kol vartotojas pasirenka nebetęsti.

# Papildoma (ekstra) užduotis:
# Pridėk dar dvi naujas operacijas:
# ^ – kelimas laipsniu
# % – liekanos (modulo) operacija


while True:
    try:
        #  Paprašome vartotojo įvesti pirmą skaičių
        skaicius1 = float(input("Įvesk pirmą skaičių: "))

        #  Pasirenkame, kokį veiksmą norime atlikti
        veiskmas = input("Įvesk veiksmą (+, -, *, /, ^, %): ")

        #  Paprašome įvesti antrą skaičių
        skaicius2 = float(input("Įvesk antrą skaičių: "))

        #  Skaičiuojame pagal pasirinktą veiksmą
        if veiskmas == "+":
            rezultatas = skaicius1 + skaicius2  # sudėtis
        elif veiskmas == "-":
            rezultatas = skaicius1 - skaicius2  # atimtis
        elif veiskmas == "*":
            rezultatas = skaicius1 * skaicius2  # daugyba
        elif veiskmas == "/":
            rezultatas = skaicius1 / skaicius2  # dalyba
        elif veiskmas == "^":
            rezultatas = skaicius1 ** skaicius2  # kelimas laipsniu
        elif veiskmas == "%":
            rezultatas = skaicius1 % skaicius2  # liekanos radimas
        else:
            #  Jei veiksmas neatpažintas – pranešame ir pradedame iš naujo
            print("Klaida! Neatpažintas veiksmas.")
            continue

        # Išvedame rezultatą į ekraną
        print("Rezultatas:", rezultatas)

    # Gaudome klaidas, kai vartotojas įveda netinkamą skaičių
    except ValueError:
        print("Klaida! Prašome įvesti tik skaičius.")
    # Gaudome dalybos iš nulio atvejį
    except ZeroDivisionError:
        print("Klaida! Dalyba iš nulio negalima.")

    # Paklausiame, ar vartotojas nori tęsti skaičiavimus
    testi = input("Ar norite tęsti? (Taip/Ne): ")
    if testi.upper() != "TAIP":
        break  # Jei ne „Taip“, nutraukiame programą
