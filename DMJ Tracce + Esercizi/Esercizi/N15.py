cont9 = 0
stringa = []
contR = 0

while cont9 < 3:
    x = int(input())
    if x >= 0 and x < 10:
        if x == 9:
            if cont9 == 2:
                cont9 += 1
            else:
                stringa.append(x)
                cont9 += 1
        else:
            stringa.append(x)
            cont9 = 0

cont3 = 0
vTemp = -1

for i in stringa:
    if i == vTemp:
        if cont3 == 2:
            contR += 1
        else:
            cont3 += 1
    else:
        vTemp = i
        cont3 = 1

print(contR, end="")
    