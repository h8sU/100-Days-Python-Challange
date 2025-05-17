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