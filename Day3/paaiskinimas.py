# ===========================================
# 📘 Paaiškinimai: Day 3 – Spėk skaičių 🎯
# ===========================================

# IMPORT
# import random – įkelia „random“ modulį, kuris leidžia generuoti atsitiktinius skaičius.
# Pvz.: random.randint(1, 100) sugeneruoja atsitiktinį skaičių nuo 1 iki 100.

# RANDOM.RANDINT()
# Sugeneruoja atsitiktinį sveikąjį skaičių iš nurodyto intervalo.
# Pvz.: slaptas = random.randint(1, 10) gali būti bet kuris skaičius nuo 1 iki 10.

# KINTAMIEJI (variables)
# Kintamieji saugo duomenis.
# Pvz.: bandymai = 0 reiškia, kad sukuriame kintamąjį, kuris saugo skaičių 0.

# WHILE TRUE
# Tai begalinis ciklas – jis kartosis tol, kol nebus nutrauktas (pvz. su „break“).
# Naudojamas tada, kai nežinome iš anksto, kiek kartų reikės kartoti veiksmą.

# INPUT()
# Leidžia vartotojui įvesti duomenis per klaviatūrą.
# Visada grąžina tekstą (string).
# Pvz.: vardas = input("Įveskite vardą: ")

# INT()
# Konvertuoja tekstą į sveikąjį skaičių (integer).
# Pvz.: spejimas = int("25") -> skaičius 25
# Jei vartotojas įveda ne skaičių – įvyksta klaida (ValueError).

# TRY / EXCEPT
# Leidžia saugiai „pagauti klaidas“ ir neleisti programai sugesti.
# Pvz.: jei vartotojas įveda raidę vietoj skaičiaus, programa sugeneruoja ValueError.

# VALUEERROR
# Ši klaida įvyksta, kai bandome neteisingai konvertuoti duomenį, pvz. int("labas").
# Programoje naudojame `except ValueError`, kad sugautume šią klaidą ir parodytume žinutę.

# IF / ELIF / ELSE
# Sąlygų tikrinimas:
# - if: kai sąlyga tenkinama.
# - elif: kita sąlyga, jei pirmoji netinkama.
# - else: jei nei viena sąlyga netinka.

# Pvz.:
# if spejimas > slaptas:
#     print("Per didelis")
# elif spejimas < slaptas:
#     print("Per mažas")
# else:
#     print("Teisingai!")

# PRINT()
# Parodo tekstą ekrane.
# Pvz.: print("Sveiki!") atspausdina „Sveiki!“ vartotojui.

# F-STRING
# Leidžia įterpti kintamuosius į tekstą naudojant f"..." sintaksę.
# Pvz.: vardas = "Jonas"; print(f"Sveikas, {vardas}!") -> „Sveikas, Jonas!“

# BREAK
# Nutraukia ciklą (pvz., while True), kai sąlyga įvykdoma.
# Naudojame, kai vartotojas atspėja teisingai.

# ==, <, > (LYGINIMO OPERATORIAI)
# == : lygina ar reikšmės yra lygios.
# <  : tikrina ar viena reikšmė mažesnė už kitą.
# >  : tikrina ar viena reikšmė didesnė už kitą.

# Pvz.:
# if spejimas == slaptas_skaicius:
#     print("Teisingai!")
