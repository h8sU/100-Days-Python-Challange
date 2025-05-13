# ===========================================
# 📘 Paaiškinimai: Day 2 CLI skaičiuoklė
# ===========================================

# KINTAMIEJI (angl. variables)
# Kintamieji yra naudojami informacijai saugoti.
# Pvz. skaicius1 = 10 reiškia, kad sukuriame kintamąjį pavadinimu skaicius1 ir jam priskiriame reikšmę 10

# INPUT()
# input() funkcija leidžia vartotojui įvesti duomenis per klaviatūrą.
# Pvz.:
# vardas = input("Įveskite savo vardą: ")
# Tai paprašys vartotojo įvesti tekstą ir saugos tai į kintamąjį vardas.

# FLOAT()
# float() funkcija konvertuoja tekstą į skaičių su kableliu (trupmeninį).
# Pvz.:
# skaicius = float("3.14") -> gausime skaičių 3.14
# Reikalinga, nes input() visada grąžina tekstą (str tipą).

# STR()
# str() konvertuoja bet kokį kintamąjį į tekstą (string).
# Pvz.:
# tekstas = str(123) -> '123'
# Dažnai naudojama, kai reikia skaičių prijungti prie sakinių.

# IF / ELIF / ELSE
# Tai sąlygos. Leidžia programai priimti sprendimus.
# Pvz.:
# if veiksmas == "+":
#     rezultatas = skaicius1 + skaicius2
# elif veiksmas == "-":
#     rezultatas = skaicius1 - skaicius2
# else:
#     print("Neatpažintas veiksmas")

# WHILE TRUE
# Begalinis ciklas, kuris kartojasi tol, kol pats jį nutrauki.
# Mes naudojame jį, kad skaičiuotuvas veiktų tol, kol vartotojas sako „Ne“.

# BREAK
# break nutraukia ciklą. Panaudojame, kai vartotojas nebenori tęsti programos.

# TRY / EXCEPT
# Tai būdas „pagauti klaidas“, kad programa nesugestų.
# Pvz. jei vartotojas vietoj skaičiaus įves raidę – programa pateiks žinutę, o ne sustos.

# VALUEERROR
# Ši klaida įvyksta, kai pvz. float() negali konvertuoti teksto į skaičių.
# Pvz. float("labas") sukels ValueError.

# ZERODIVISIONERROR
# Ši klaida įvyksta, jei bandoma padalyti iš 0.
# Pvz. 5 / 0 – neleidžiama, nes matematikoje tai negalima.

# OPERATORIAI: +, -, *, /, ^, %
# + : sudėtis
# - : atimtis
# * : daugyba
# / : dalyba
# ^ : laipsnio kėlimas (naudojame **, pvz. 2 ** 3 = 8)
# % : liekana (modulo), pvz. 5 % 2 = 1 (lieka 1)

# UPPER()
# Tai string (teksto) metodas, kuris visas raides paverčia didžiosiomis.
# Pvz. "taip".upper() -> "TAIP"
# Naudojame tam, kad palyginimas būtų lankstesnis (nepriklausytų nuo raidžių dydžio).

# Pavyzdys:
# testi = input("Ar norite tęsti? (Taip/Ne): ")
# if testi.upper() != "TAIP":
#     break  # išeiname iš ciklo
