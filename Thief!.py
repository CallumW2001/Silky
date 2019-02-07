
import random

pin = int(input("Please Enter Your 4-Digit PIN Number : "))

while (len(str(pin)) < 4 or len(str(pin))) > 4:

    pin = int(input("Please Enter Your 4-Digit PIN Number : "))

pinlist = list(str(pin))

print(pinlist)
print(pinlist[0])
print(pinlist[1])
print(pinlist[2])
print(pinlist[3])

combolist = []

combo = 0

while len(combolist) < 40:

    x = 0
    y = 0
    z = 0
    f = 0

    while (x == y or x == z or x == f or y == z or y == f or z == f):

        x = random.randint(0,3)
        y = random.randint(0,3)
        z = random.randint(0,3)
        f = random.randint(0,3)

        combo = (pinlist[x], pinlist[y], pinlist[z], pinlist[f])
        

        if (combo not in combolist):
        
            combolist.append(combo)
            break


        elif(combo in combolist):

            print()


print(len(combolist))
print()
print(combolist)

