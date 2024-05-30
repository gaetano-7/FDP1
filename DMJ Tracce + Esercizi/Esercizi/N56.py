dim=20
pavimento=[]
pi=0
pj=0
alta=False
bassa=True
com=0
listacom=[]

for i in range(dim):
    pavimento.append([])
    for j in range(dim):
        pavimento[i].append(0)

while com!=9:
    com=int(input())
    if (com>0 and com<8) and len(listacom)<100:
            listacom.append(com)
    if com==1: #ALZA
        bassa=False
        alta=True
            
    elif com==2: #ABBASSA
        bassa=True
            
    elif com==3: #EST
        passi=int(input("passi?"))
        print()
        for i in range(passi):
            if pj+1<len(pavimento):
                pj+=1
                pavimento[pi][pj]
                if bassa:
                    pavimento[pi][pj]=1
                            
    elif com==4: #OVEST
        passi=int(input("passi?"))
        print()
        for i in range(passi):
            if pj-1>=0:
                pj-=1
                pavimento[pi][pj]
                if bassa:
                    pavimento[pi][pj]=1
            
    elif com==5: #SUD
        passi=int(input("passi?"))
        print()
        for i in range(passi):   
                if pi+1<len(pavimento):
                    pi+=1
                    pavimento[pi][pj]
                    if bassa:
                        pavimento[pi][pj]=1
            
    elif com==6: #NORD
        passi=int(input("passi?"))
        print()
        for i in range(passi):
            if pi-1>=0:
                pi-=1
                pavimento[pi][pj]
                if bassa:
                    pavimento[pi][pj]=1
            
    elif com==7: #STAMPA
        for i in range(dim):
            for j in range(dim):
                if pavimento[i][j]==1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        
    elif com==8:
        continue
    
    elif com==9:
        tappo=0
