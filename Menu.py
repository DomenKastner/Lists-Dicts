# -*- coding: utf-8 -*-

# Program za vnos ter izpis jedilnika

menu = dict()

while True:

    jed = raw_input("Vpiši jed: ")  # Vpišem jed
    print "Vpisali ste: " + jed

    cena = raw_input("Vpiši ceno: ")  # Vpišem ceno
    print "Vnesli ste: " + cena + " €"

    menu[jed + cena] = cena  # <--- Tega ne razumem kaj to naredi ?

    for item in menu:  # od nekaj v meni (dict) naprinta v naslednjo vrstico naš vnos
            print jed + " " + cena + " €"

    dodati = raw_input("Bi dodali še kakšno jed (y/n)?: ")  # Vpraša po ponovitvi
    if dodati != "y":
        break

natisni = raw_input("Želite natisniti cenik (y/n) :")
if natisni == "y":
        menu = open("Menu.txt", "w+")  # open the TXT file (or create a new one)
        print "cenik:"
        menu.write("cenik\n" + "-" + jed + " " + cena)  # write into the TXT file

print "Dober tek"

# -----------------------------------------------------------------------------------#

# Ko dodajam novo jed mi prejšnjo prepiše z novo vrednostjo?

# Ne zastopim kaj naredi 14 vrstica. Brez tega ne shrani v meni?

# Ampak shrani le zadnjo vnešeno?
