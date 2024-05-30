from random import randint
def main():
    s=str(input("scegli la dimensione dello schema su quale vuoi giocare (da 4*4 a 9*9): "))
    N=int(s[0])
    print(N)
    griglia=crea_griglia(N)
    printa(griglia,N)
    controlla(griglia,N)
    gioco(N,griglia)

def crea_griglia(N):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(N):
            f=randint(0,1)
            if f==0:
                m[i].append("of")
            elif f==1:
                m[i].append("on")
    return m

def printa(griglia,N):
    for i in range(N):
        print(griglia[i])

def corrente(griglia,i,j):
    if griglia[i][j]=="on":
        griglia[i][j]="of"
    elif griglia[i][j]=="of":
        griglia[i][j]="on"

def destra(griglia,i,j):
    if griglia[i][j+1]=="on":
        griglia[i][j+1]="of"
    elif griglia[i][j+1]=="of":
        griglia[i][j+1]="on"

def sinistra(griglia,i,j):
    if griglia[i][j-1]=="on":
        griglia[i][j-1]="of"
    elif griglia[i][j-1]=="of":
        griglia[i][j-1]="on"
    

def sù(griglia,i,j):
    if griglia[i-1][j]=="on":
        griglia[i-1][j]="of"
    elif griglia[i-1][j]=="of":
        griglia[i-1][j]="on"

def giù(griglia,i,j):
    if griglia[i+1][j]=="on":
        griglia[i+1][j]="of"
    elif griglia[i+1][j]=="of":
        griglia[i+1][j]="on"

def controlla(griglia,N):
    l=[]
    for i in range(N):
        for j in range(N):
            l.append(griglia[i][j])
    c=0
    for i in range(len(l)):
        if "on" not in l:
            c=1
    return c

def gioco(N,griglia):
    while controlla(griglia,N)!=1:
        i=int(input())
        j=int(input())
        if i==0 and j!=0 and j!=N-1: #prima riga
            corrente(griglia,i,j)
            giù(griglia,i,j)
            destra(griglia,i,j)
            sinistra(griglia,i,j)
        if i==N-1 and j!=0 and j!=N-1: #ultima riga
            corrente(griglia,i,j)
            sù(griglia,i,j)
            destra(griglia,i,j)
            sinistra(griglia,i,j)
        if j==0 and i!=0 and i!=N-1: #prima colonna
            corrente(griglia,i,j)
            sù(griglia,i,j)
            giù(griglia,i,j)
            destra(griglia,i,j)
        if j==N-1 and i!=0 and i!=N-1: #ultima colonna
            corrente(griglia,i,j)
            sù(griglia,i,j)
            giù(griglia,i,j)
            sinistra(griglia,i,j)
        if i==0 and j==0: #angolo sx-alto
            corrente(griglia,i,j)
            giù(griglia,i,j)
            destra(griglia,i,j)
        if i==0 and j==N-1: #angolo dx-alto
            corrente(griglia,i,j)
            giù(griglia,i,j)
            sinistra(griglia,i,j)
        if i==N-1 and j==0: #angolo sx-basso
            corrente(griglia,i,j)
            sù(griglia,i,j)
            destra(griglia,i,j)
        if i==N-1 and j==N-1: #angolo dx-basso
            corrente(griglia,i,j)
            sù(griglia,i,j)
            sinistra(griglia,i,j)
        if i!=0 and i!=N-1 and j!=0 and j!=N-1:
            corrente(griglia,i,j)
            giù(griglia,i,j)
            destra(griglia,i,j)
            sinistra(griglia,i,j)
        printa(griglia,N)

main()