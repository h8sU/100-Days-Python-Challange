# ===========================================
# 🟢 Day 1: Hello World + spalvotas ir animuotas pasisveikinimas
# ===========================================

# Užduotis:
# Sukurk skriptą, kuris atspausdina „Hello, Python!“ spalvotai ir su animacija 
# (pvz. raidės atsiranda po vieną, su trumpu laukimu tarp jų).

# ===========================================
# NAUDOJAMI ELEMENTAI IR KĄ JIE DARO:
# ===========================================

# PRINT()
# Tai pagrindinė funkcija, skirta atvaizduoti tekstą ekrane.
# Pvz.:
# print("Hello, world!") – parodys tekstą terminale.

# FOR CIKLAS
# Leidžia kartoti veiksmus kiekvienam simboliui ar reikšmei.
# Pvz.:
# for raide in "Labas": print(raide)
# Tai atspausdins kiekvieną raidę atskirai.

# TIME.SLEEP()
# Laikinas laukimas tarp veiksmų.
# Pvz.:
# time.sleep(0.2) – palaukia 0.2 sekundės.
# Naudojama animacijai – raidės atsiranda po vieną.

# END PARAMETRAS PRINT FUNKCIJOJE
# Pagal nutylėjimą `print()` po kiekvieno iškvietimo perkelia eilutę žemyn.
# Jei norime, kad tekstas tęstųsi toje pačioje eilutėje, naudojame:
# print("a", end="") – neatliekamas naujos eilutės perkėlimas.

# COLORAMA BIBLIOTEKA
# Naudojama tekstui spalvinti terminale (Windows/Linux/Mac).
# Pavyzdys:
# from colorama import Fore
# print(Fore.RED + "Raudonas tekstas")

# INIT() iš COLORAMA
# from colorama import init – tai paleidžia biblioteką, kad spalvos veiktų Windows sistemoje.

# SPALVOS (Fore)
# Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN ir pan. – nurodo teksto spalvą.

# RESET()
# Naudojama po spalvoto teksto, kad po jo sekantis tekstas vėl būtų normalus (nespalvotas).

# =============================
# PAPILDOMA:
# =============================
# Galima naudoti emoji 😎, spalvas arba `\n` (nauja eilutė) efektui sustiprinti.
# Galima išplėsti animaciją naudojant `sys.stdout.write()` ir `sys.stdout.flush()` – jei norima dar labiau valdyti išvedimą.
