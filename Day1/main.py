# ===============================
#  Day 1: Hello World projektas
# ===============================

# Tikslas:
# Sukurti Python programą, kuri terminale atspausdina tekstą
# „Hello, Python!“ po vieną raidę, su animacija ir spalva.

# Importuojame reikalingas bibliotekas
import time                          # Laiko valdymui (naudojamas laukimui tarp raidžių)
from colorama import init, Fore     # Teksto spalvinimui terminale

# Inicializuojame colorama (reikalinga, kad spalvos veiktų Windows sistemoje)
init()

# Tekstas, kurį norime animuoti
tekstas = "Hello, Python!"

# Spalva, kuri bus naudojama tekstui
spalva = Fore.CYAN

# Eikime per kiekvieną simbolį tekste ir atspausdinkime jį su animacija
for raide in tekstas:
    print(spalva + raide, end="", flush=True)  # flush=True užtikrina, kad raidė pasirodytų iškart
    time.sleep(0.1)  # laukiam 0.1 sekundės tarp raidžių

# Atstatome spalvas į įprastas
print(Fore.RESET)
