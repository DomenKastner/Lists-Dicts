# -*- coding: utf-8 -*-

opravila = dict()

opravila2 = [
    ["nekaj", True],
    ["Drugo", False],
    ["Tretje opravilo", True]
]

while 1:
    task = raw_input("vpisi naslednje opravilo:")
    opravil = raw_input("si to ze opravil (y/n)?")
    if opravil == "y":
        opravila[task] = True
    else:
         opravila[task] = False

    #opravila.append(task)

    nadaljuj = raw_input("Zelis nadaljevati (y/n)")

    if nadaljuj == "n":
        break

print("TODO List:")
st_opravljenih = 0
st_neopravljenih = 0

for nekaj in opravila:
    print(nekaj, opravila[nekaj])

    if opravila[nekaj] == True:
        st_opravljenih = st_opravljenih +1
        print ("ze opravil")

    else:
        st_neopravljenih = st_neopravljenih +1
        print("to moras se postoriti")

print(st_opravljenih)
print(st_neopravljenih)

#for opr in opravila:
    #print(opr)

#for mesto in range(len(opravila)):
    #print str(mesto+1) + ". " + str(opravila[mesto])
#mesto+1 je zato, da prvi vpis ni na mestu 0

#print("to so vsa opravila za danes")


#BONUS...


todo_file = open("Practice_task_Dict.txt", "w+")  # open the TXT file (or create a new one)

print "Dokončana opravila:"
todo_file.write("Dokončana opravila:\n")  # write into the TXT file
for nekaj in opravila:
    if opravila[nekaj] == True:
        print "- " + nekaj
        todo_file.write("- " + nekaj + "\n")  # add task into the TXT file

todo_file.write("\n")

print "Nedokončana opravila:"
todo_file.write("Nedokončana opravila:\n")  # write into the TXT file
for nekaj in opravila:
    if opravila[nekaj] == False:
        print "- " + nekaj
        todo_file.write("- " + nekaj + "\n")  # add task into the TXT file

todo_file.close()  # close the TXT file