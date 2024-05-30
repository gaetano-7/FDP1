l=""
x=0
y=0

while x!=-1:
    n=int(input())
    if n != -1:
        if n >= 0 and n <= 9:
            l += str(n)
        else:
            y += 1
    else:
        x = -1

if y != 0:
    print("ERRORE", end="")
elif len(l) == 0:
    print("VUOTO", end="")
else:
    if int(l)%3 == 0:
        print(l)
        print("SI", end="")
    else:
        print(l)
        print("NO", end="")