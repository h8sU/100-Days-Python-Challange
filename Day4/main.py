# Day 4: Amžiaus patikrinimo programa
# Vartotojas įveda savo gimimo metus, programa paskaičiuoja amžių ir pasako ar vartotojas pilnametis

# Paprasta „Ar galiu eiti į kiną?“ logika
# Įvedus amžių, programa pasako ar vartotojas gali eiti į kiną (pagal nustatytą amžiaus ribą)


from datetime import datetime

#Gauname dabartini laika
dabartiniai_metai = datetime.now().year
amziaus_leidimas = 16
try:
    # Vartoto ivestis: gimimo metai
    gimimo_metai = int(input("Iveskite savo gimimo metus: "))
    amzius = dabartiniai_metai - gimimo_metai
    print(f"Tau dabar yra: {amzius} metai.")

    if gimimo_metai > dabartiniai_metai:
        print("Klaida! Tu dar nesi gimes.")
    elif amzius < amziaus_leidimas: 
        print(f"Tau dar nera {amziaus_leidimas} metu! Deja dar tau negalima")
    else:
        print("Valio! Tu gali uzeiti!")

except ValueError:
    print("Klaida, iveskite tik gimimo metus!")

