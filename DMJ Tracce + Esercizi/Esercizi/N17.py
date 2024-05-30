M=0
N=-468461
trovato=False
while True:
    M=N
    N=int(input())

    if(N==0):
        break

    if(M%2==0 and N%2==0):
        trovato=True
    elif((M+N)%M ==0):
        trovato=True
    elif((M+N)%N==0):
        trovato=True

if (trovato):
    print("SI",end="")
else:
    print("NO",end="")
    
