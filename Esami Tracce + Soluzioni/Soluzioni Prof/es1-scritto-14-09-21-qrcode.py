from random import randint

def genera_e_controlla_totale(N,Tot_min,Tot_max):
    tot=0
    qrcode=[]
    for i in range(N):
        riga=[]
        for j in range(N):
            x=randint(0,1)
            if x==1:
                riga.append("*")
            else:
                tot+=1
                riga.append(" ")
        qrcode.append(riga)
    if not(tot<=Tot_max and tot>=Tot_min):
        return []
    return qrcode

def controlla_righe(qrcode,N,R_min,R_max):
    for i in range(N):
        tot_riga=0
        for j in range(N):
            if qrcode[i][j]==" ":
                tot_riga+=1
        if not(tot_riga<=R_max and tot_riga>=R_min):
            return False
    return True

def controlla_colonne(qrcode,N,C_min,C_max):
    for j in range(N):
        tot_colonna=0
        for i in range(N):
            if qrcode[i][j]==" ":
                tot_colonna+=1
        if not(tot_colonna<=C_max and tot_colonna>=C_min):
            return False
    return True

N=3
R_min=1
R_max=2
C_min=1
C_max=2
Tot_min=3
Tot_max=7
T=10

# N=int(input())
# R_min=int(input())
# R_max=int(input())
# C_min=int(input())
# C_max=int(input())
# Tot_min=int(input())
# Tot_max=int(input())
# T=int(input())

tentativi=0
while tentativi<T:
    
    qrcode=genera_e_controlla_totale(N,Tot_min,Tot_max)
    if qrcode==[]:
        tentativi+=1
        continue
    
    if not controlla_righe(qrcode,N,R_min,R_max):
        tentativi+=1
        continue
    
    if not controlla_colonne(qrcode,N,C_min,C_max):
        tentativi+=1
        continue

    for i in range(N):
        for j in range(N):
            print(qrcode[i][j],end=" ")
        print()
    break