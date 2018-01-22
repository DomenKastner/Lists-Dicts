# -*- coding: utf-8 -*-
meni = dict()

meni2 = [
    ["nekaj", True],
]

while True:

    jed = raw_input("Vpiši vrsto jedi:")
    cena = int(raw_input("Vpiši ceno jedi:"))

    dodal = raw_input("Bi dodal še kakšno jed (y/n)?")

    if dodal == "y":
        meni[jed, cena] = True
    else:
        break

prin = raw_input("Zelis natisniti meni (y/n)")

if prin == "y":

    print("menu:")
    jed= 0
    cena = 0

    for nekaj in meni:
        print(nekaj, meni[nekaj])

        if meni[nekaj] == True:
            cena = cena +1
            print ("Jed")

        else:
            jed = jed +1
            print("cena")

    print(jed)
    print(cena)


    todo_file = open("menu.txt", "w+")  # open the TXT file (or create a new one)

    print "Jed:"
    todo_file.write("Jed:\n")  # write into the TXT file
    for jed in meni:
        if meni[jed] == True:
            print "- " + jed
            todo_file.write("- " + jed + "\n")  # add task into the TXT file

    todo_file.write("\n")

    print "Cena:"
    todo_file.write("Cena:\n")  # write into the TXT file
    for cena in meni:
        if meni[cena] == False:
            print "- " + cena
            todo_file.write("- " + cena + "\n")  # add task into the TXT file