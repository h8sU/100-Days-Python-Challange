# 🧠 Python viktorina

# A B C D - atsakymi variantai 
# Tasku sistema su vertinimu. (Puikiai, gerai, vidutiniskai, yra dar kur tobuleti)

klausimai = [
    {
        "klausimas": "1. Kam naudojamas 'if' sakinys?",
        "pasirinkimai": {
            "A": "Pakartojimo komanda",
            "B": "Sąlygos patikrinimas",
            "C": "Komentaras",
            "D": "Kodo išvalymas"
        },
        "atsakymas": "B"
    },
    {
        "klausimas": "2. Ką daro funkcija print()?",
        "pasirinkimai": {
            "A": "Įveda duomenis",
            "B": "Sustabdo programą",
            "C": "Išveda tekstą",
            "D": "Sukuria kintamąjį"
        },
        "atsakymas": "C"
    },
    {
        "klausimas": "3. Kuo skiriasi list ir tuple?",
        "pasirinkimai": {
            "A": "tuple keičiamas, list – ne",
            "B": "list keičiamas, tuple – ne",
            "C": "abu keičiasi",
            "D": "nė vienas nekeičiami"
        },
        "atsakymas": "B"
    },
    {
        "klausimas": "4. Koks rezultatas: 5 // 2?",
        "pasirinkimai": {
            "A": "2.5",
            "B": "2",
            "C": "3",
            "D": "2.0"
        },
        "atsakymas": "B"
    },
    {
        "klausimas": "5. Kuri reikšmė yra 'boolean' tipo?",
        "pasirinkimai": {
            "A": "5",
            "B": "„True“",
            "C": "'hello'",
            "D": "[]"
        },
        "atsakymas": "B"
    },
    {
        "klausimas": "6. Ką daro funkcija input()?",
        "pasirinkimai": {
            "A": "Suskaičiuoja simbolius",
            "B": "Išveda duomenis",
            "C": "Įveda duomenis",
            "D": "Uždaro programą"
        },
        "atsakymas": "C"
    },
    {
        "klausimas": "7. Kaip sukuriama funkcija?",
        "pasirinkimai": {
            "A": "function mano():",
            "B": "create mano():",
            "C": "def mano():",
            "D": "func mano():"
        },
        "atsakymas": "C"
    },
    {
        "klausimas": "8. Koks simbolis naudojamas komentarams?",
        "pasirinkimai": {
            "A": "//",
            "B": "##",
            "C": "#",
            "D": "--"
        },
        "atsakymas": "C"
    },
    {
        "klausimas": "9. Kaip aprašyti sąrašą su trim reikšmėm?",
        "pasirinkimai": {
            "A": "[1, 2, 3]",
            "B": "(1, 2, 3)",
            "C": "{1, 2, 3}",
            "D": "<1, 2, 3>"
        },
        "atsakymas": "A"
    },
    {
        "klausimas": "10. Kaip parašyti 'for' ciklą nuo 1 iki 5?",
        "pasirinkimai": {
            "A": "for i in 1 to 5:",
            "B": "for i = 1 to 5:",
            "C": "for i in range(1, 6):",
            "D": "repeat 5 times"
        },
        "atsakymas": "C"
    },
]

# Pradinis tasku skaicius
taskai = 0 


# Pagrindinis ciklas 
for k in klausimai:
    print("\n" + k["klausimas"])
    for key, value in k["pasirinkimai"].items():
        print(f" {key}) {value}")

    vartotojo_atsakymas = input("Tavo atsakymas (A/B/C/D): ").strip().upper()

    if vartotojo_atsakymas == k["atsakymas"]:
        print("✅ Teisingai!")
        taskai += 1
    else: 
        print(f"❌ Neteisingi! Teisingas atsakymas buvo {k['atsakymas']}) {k['pasirinkimai'][k['atsakymas']]}")

# Rezultato apzvalga 
print("\n 🧾 Viktorina baigta!")
print(f" 🎯 Surinkai {taskai} is {len(klausimai)} tasku")

# Tasku vertinimo logika
if taskai == 10:
    print("🏆 Puikiai! Esi tikras Python asas!")
elif taskai >= 7:
    print(f"👍 Gerai padibeta! Dar siek tiek praktikos ir bus puikiai!")
elif taskai >= 4: 
    print(f"🤓 Ne blogai, bet varta pakartoti pagrindus!")
else:
    print(f" Laikas pasimokyti is naujo! Viskas imanoma! 💪")