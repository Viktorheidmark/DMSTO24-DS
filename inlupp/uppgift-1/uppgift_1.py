# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(x: int) -> bool:
#beräknar resten efter en division av två heltal?
    return x % 2 != 0

print (is_odd(1))
print (is_odd(2))
print (is_odd(3))
print (is_odd(0))
print (is_odd(-1))
print (is_odd(-2))