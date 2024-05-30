def leggiTabella(r, c):
    tabella = []
    for i in range(r):
        tabella.append([])
        for j in range(c):
            tabella[i].append(input("Inserire carattere "))
    for i in range(r):
        print(tabella[i])
    return tabella

def leggiLunghezze(l):
    lunghezze = []
    for i in range(l):
        lunghezze.append(int(input("Inserire la lunghezza della prossima parola ")))
    return lunghezze

def trovaSequenzeValide(sequenza,tabella):
    sv = []
    for i in range(len(sequenza)-2):
        if sequenza[i].isdigit() and sequenza[i+1].isdigit() and (sequenza[i+2] == 'o' or sequenza[i+2] == 'v'):
            r=int(sequenza[i])
            c=int(sequenza[i+1])
            if (r<len(tabella) and c<len(tabella[0])):
                if sequenza[i+2] == 'o' and (c==0 or tabella[r][c-1]=='*'):
                    sv.append([r,c,sequenza[i+2]])
                elif sequenza[i+2] == 'v' and (r==0 or tabella[r-1][c]=='*'):
                    sv.append([r,c,sequenza[i+2]])
    return sv

def paroleNascoste(tabella, lunghezze, sequenzeValide):
    parole = []
    n = 0
    for i in range(len(sequenzeValide)):
        if n == len(lunghezze):
            break
        
        r = sequenzeValide[i][0]
        c = sequenzeValide[i][1]
    
        if sequenzeValide[i][2] == 'o': 
            if ((c + lunghezze[n]) > len(tabella[0])) or ((c + lunghezze[n]) < len(tabella[0]) and tabella[r][(c+lunghezze[n])]!='*'):
                continue
            parola = ""
            j=0
            while (c+j)<len(tabella[0])and tabella[r][c+j]!='*':
                parola += tabella[r][c+j]
                j+=1

            if len(parola)==lunghezze[n]:
                parole.append(parola)
                n += 1

        elif sequenzeValide[i][2] == 'v':
            if ((r + lunghezze[n]) > len(tabella)) or ((r + lunghezze[n]) < len(tabella) and tabella[(r+lunghezze[n])][c]!='*'):
                continue
            parola = ""
            j=0
            while ((r+j)<len(tabella) and tabella[r+j][c]!='*'):
                parola += tabella[r+j][c]
                j+=1

            if len(parola)==lunghezze[n]:
                parole.append(parola)
                n += 1

    return parole

def main():
    # Lettura tabella caratteri
    r = int(input("Inserire il numero di righe della tabella: "))
    c = int(input("Inserire il numero di colonne della tabella: "))
    tabella = leggiTabella(r, c)

    # Lettura lista lunghezze parole
    n = int(input("Inserire il numero di parole per le quali leggere le lunghezze: "))
    lunghezze=leggiLunghezze(n)
    # Lettura testo posizioni nascoste
    pn = input("Inserire la stringa che codifica le posizioni delle parole nascoste ")

    sequenzeValide = trovaSequenzeValide(pn,tabella)
    
    print(sequenzeValide)
    
    frase=paroleNascoste(tabella, lunghezze, sequenzeValide)
    
    if (len(frase)==len(lunghezze)):
        print("La frase nascosta e': ", end='')
        for i in range(len(frase)):
            print (frase[i],' ',end='')
    else:
        print("Nessuna frase nascosta")

main()