crescente=0
last=""
while True:
    x=int(input())
    if x == 0:
        break

    if (crescente == 0):  
        if (last != ""):  
            if (last < x):
                crescente = 1  
            else:
                crescente = 3 
    elif (crescente == 1):  
        if (last >= x):
            crescente = 2

    elif (crescente == 2):  
        if (last <= x):
            crescente = 3  

    last = x

if crescente == 2:
    print("SI", end="")
else:
    print("NO",end="")
