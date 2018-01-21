# -*- coding: utf-8 -*-

opravila = []

opravila2 = [
    ["neakj", True],
    ["Drugo", False],
    ["Tretje opravilo", True]
]

while 1:
    task = raw_input("vpisi naslednje opravilo:")
    opravil = raw_input("si to ze opravil (y/n)?")
    if opravil == "y":
        opravila.append([task, True])
    else:
         opravila.append([task, False])

    #opravila.append(task)

    nadaljuj = raw_input("Zelis nadaljevati (y/n)")

    if nadaljuj == "n":
        break

print("TODO List")

#for opr in opravila:
    #print(opr)

for mesto in range(len(opravila)):
    print str(mesto+1) + ". " + str(opravila[mesto])
#mesto+1 je zato, da prvi vpis ni na mestu 0

print("to so vsa opravila za danes")