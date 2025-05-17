# Day 5: Teksto analizatorius: 

#    Įvedi tekstą:
#    programa suskaičiuoja:
#    kiek yra raidžių, 
#    žodžių, 
#    sakinių


# isalpha() - Ar simbolis yra raide

#print('a'.isalpha()) # True
#print('1'.isalpha()) # False

# Kas yra sarasas - 

# sarasas = ['vardas', 'pavarde', 1, 2.3, True]
# print(sarasas[6])
# Prasideda ne nuo 1 o nuo 0


#join - ''.joint([])

# simboliai = ['L', 'A', 'B', 'A', 'S']
# tekstas = ''.join(simboliai)
# print(tekstas)

# .split()
# print("Labas pasauli!".split()) # ['Labas', 'pasauli!']

# re.split(r')

# re_split = re.split(r'[.!?]+', "Labas! Kaip tau sekasi? Gerai.") 
# print(re_split)

# strip() - Prasalina tarpus pradzioje ir gale 

# split = "   Labas    " .strip() # "Labas"
# print(split)

# def - funkcija 
#def sudetis(skaicius1, skaicius2):
#    return print(skaicius1 + skaicius2)
#
# sudetis(1, 5)
# sudetis(1, 2)

# len() - Skaiciuoja elemtus

# print(len("Labas! ")) # 7
# print(len(['a', 'b'])) # 2


### --- Kodas --- ### 

import string
import re 

def analizatorius_teksto(tekstas):
    """
    Funkcija analizuoja pateiktus teksta ir grazina:
    - raidziu skaiciu (Be tarpu ir skyrybos zenklu)
    - zodziu kieki (skaiciumi)
    - sakiniu skaiciu.
    """

    # Pasalinkime visus ne reikalingus simbolius palikdami tik raides
    tik_raide = ''.join(simbolis for simbolis in tekstas if simbolis.isalpha())
    raidziu_skaicius = len(tik_raide)
    
    # Naudodami .split() metoda, kuris dalins pagal tarpus
    zodziai = tekstas.split()
    zodziu_skaicius = len(zodziai)

    # Sakinius nustatome pagal taska, klaustuka arba saktuka naudodami regex

    sakiniai = re.split(r'[.!?]+', tekstas)
    #Pasalinkime tuscias eilute
    sakiniai = [s for s in sakiniai if s.strip()]
    sakiniu_skaicius = len(sakiniai)


    print(f"""
Tavo teksto analize: \n
Raidziu kiekis tekste: {raidziu_skaicius}. \n
Zodziu kiekis teksta: {zodziu_skaicius}.\n
Tavo tekste yra viso: {sakiniu_skaicius} sakiniai.
""")
    

## Testavimas 

analizatorius_teksto("Aciu! Kad ziurejai ir iki kito karto!")