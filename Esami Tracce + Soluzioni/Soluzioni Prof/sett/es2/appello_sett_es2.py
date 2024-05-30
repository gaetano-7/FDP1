N=int(input())
mat=[]    #creare la matrice vuota
if N>=1 and N<=10:   
    for i in range(N):   #per ogni riga
        mat.append([])   #aggiungere la riga vuota alla matrice
        for j in range(N): #per ogni colonna
            mat[i].append(int(input())) #e aggiungiamo gli elementi

lilla=False    #all'inizio diciamo che la condizione è Falsa

for i in range(N):   #indice i per controllare le righe    
    for j in range(N): #indice j per controllare le colonne
        for k in range(j+1,N): #ogni elemento [i][j] devo confrontarlo con quello successivo, quindi con questo for considero i suoi successivi
            if mat[i][j]==mat[i][k]: #se l'elemento [i][j] è uguale al successivo: [i][k]
                lilla=True  #condizione divent True

for j in range(N): #indice j per controllare le colonne
    for i in range(N): #indice i per controllare le righe
        for k in range(i+1,N): #k per confrontare l'elemento succ. (i+1)
            if mat[i][j]==mat[k][j]: #se l'elemento [i][j] è uguale al successivo: [k][j]
                lilla=True #condizione diventa True
                
if lilla:
    print("NO",end="")     
else:
    print("NO",end="")

    