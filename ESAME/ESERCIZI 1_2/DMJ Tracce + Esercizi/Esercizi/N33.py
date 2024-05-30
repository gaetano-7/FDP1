import random
from random import randint
random.seed(0)

vinceGiocatore=0
VincePc=0

while vinceGiocatore<3 and VincePc<3:
    giocata=int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    
    if giocata > 3 or giocata < 1:
        continue
    
    giocataPc=randint(1,3)
    
    if giocata==1:
        print("hai giocato sasso")
    elif giocata==2:
        print("hai giocato carta")
    elif giocata==3:
        print("hai giocato forbice")
        
    if giocataPc==1:
        print("il PC ha giocato sasso")
    elif giocataPc==2:
        print("il PC ha giocato carta")
    elif giocataPc==3:
        print("il PC ha giocato forbice")

    if giocata==giocataPc:
        print("Pari:")
    
    if giocata==1:
        if giocataPc==2:
            print("Vince il PC:")
            VincePc+=1
        elif giocataPc==3:
            print("Vinci tu:")
            vinceGiocatore+=1
            
    if giocata==2:
        if giocataPc==1:
            print("Vinci tu:")
            vinceGiocatore+=1
        elif giocataPc==3:
            print("Vince il PC:")
            VincePc+=1
            
    if giocata==3:
        if giocataPc==1:
            print("Vince il PC:")
            VincePc+=1
        if giocataPc==2:
            print("Vinci tu:")
            vinceGiocatore+=1
            
    print(str(vinceGiocatore)+"-"+str(VincePc))
    
if vinceGiocatore==3:
    print("Hai vinto la sfida!")
else:
    print("Il PC ha vinto la sfida!")