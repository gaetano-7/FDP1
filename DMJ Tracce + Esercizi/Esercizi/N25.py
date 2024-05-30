cont=0
seq=0
somma=[]

while cont!=2:
    n=int(input())
    if n==0:
        cont+=1
        if cont==2:
            break
        else:
            somma.append(seq)
            seq=0
    else:
        seq+=n
        cont=0
        
for i in somma:
    print(i)