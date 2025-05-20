# Day 8: Slaptazodzio generatorius

"""
Dvi funkcijos def()
 - slaptazodzio_generatorius(...)
 - slaptazodzio_stiprumo_patikrinimas()

Input:
 - kokio ilgio slaptzodis (pvz 12)
 - Ar naudoti didziasias raides
 - ar naudoti mazases raide
 - ar naudoti speceliuosius simboliu
 - ar naudot skaicius 

"""

# Bibliotekos random ir string

""" import random

rand = random.choice("ABCD") # Grazinti viena is raidziu A, B, C arba D
print(rand) """


""" import string 


print(string.ascii_letters) # Grazins sarasa ABCD...
print(string.ascii_uppercase) # Grazins tik didziasias raides
print(string.ascii_lowercase) # Grazin mazases
print(string.digits) # Grazins 0123456789
print(string.punctuation) # Grazins sarasa spceliuju simboliu """


"""
pool = "Didzios, mazosios, ...."
"""

"""
taskai = 0 / Klaida turi buti bent vienas pasirinktas elementu tipas
"""


### --- Kodas --- ### 

import random
import string

def slaptazodzio_generatorius(ilgis, naudit_didziases, naudoti_mazases, naudti_skaicius, naudoti_spec_simbolius):
    pool = ""
    if naudit_didziases: 
        pool += string.ascii_uppercase
    if naudoti_mazases:
        pool += string.ascii_lowercase
    if naudti_skaicius: 
        pool += string.digits
    if naudoti_spec_simbolius:
        pool += string.punctuation

    if not pool:
        print("Klaida! Pasirink bent viena simboliu tipa")

    slaptazodis = "".join(random.choice(pool) for _ in range(ilgis))
    return slaptazodis

def slaptazodzio_stiprumo_patikra(slaptazodis):
    taskai = 0

    if len(slaptazodis) >= 12: taskai += 1
    if any(c.islower() for c in slaptazodis): taskai += 1
    if any(c.isupper() for c in slaptazodis): taskai += 1
    if any(c.isdigit() for c in slaptazodis): taskai += 1
    if any(c in string.punctuation for c in slaptazodis): taskai += 1

    if taskai <= 2:
        return "Silpnas"
    elif taskai == 3:
        return "Vidutinis"
    else: 
        return "Stiprus"


# --- Vartotojo sasaja (Terminale) --- #
print("🔐 Slaptazodzio generatorius")
try:
    ilgis = int(input("Ivesk slaptazodzio ilgi: "))
except ValueError:
    print("❗Klaida! Iveskite skaiciu!")

def taip_ne(klausimas):
    return input(klausimas + " (Taip/Ne) ").lower() in ["taip", "t", "y"]

naudoti_didziasias = taip_ne("Ar naudoti didziasias raides?: ")
naudoti_mazasias = taip_ne("Ar naudoti mazases raides?: ")
naudoti_skaicius = taip_ne("Ar naudoti skaicius?: ")
naudoti_spec_simbolius = taip_ne("Ar naudoi spec. simbolius?: ")

slaptazodis = slaptazodzio_generatorius(ilgis, naudoti_didziasias, naudoti_mazasias, naudoti_skaicius, naudoti_spec_simbolius)

if " ! " in slaptazodis:
    print(slaptazodis)
else: 
    print(f"✅ Sugeneruotas slaptazodis {slaptazodis}")
    print(f"🛡️ Stiprumas:" + slaptazodzio_stiprumo_patikra(slaptazodis))