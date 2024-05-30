def sud(n,m,matrice):
    for i in range(n-1):
        for j in range(m):
            if matrice[i][j] == 0 or matrice[i][j] == 3:
                if j>0 and matrice[i+1][j-1] == 1:
                    matrice[i+1][j-1] = 3
                if matrice[i+1][j] == 1:
                    matrice[i+1][j] = 3
                if j<m-1 and matrice[i+1][j+1] == 1:
                    matrice[i+1][j+1] = 3
    return matrice

def nord(n,m,matrice):
    for i in range(n-1,0,-1):
        for j in range(m):
            if matrice[i][j] == 0 or matrice[i][j] == 3:
                if j>0 and matrice[i-1][j-1] == 1:
                    matrice[i-1][j-1] = 3
                if matrice[i-1][j] == 1:
                    matrice[i-1][j] = 3
                if j<m-1 and matrice[i-1][j+1] == 1:
                    matrice[i-1][j+1] = 3
    return matrice

def est(n,m,matrice):
    for j in range(m-1):
        for i in range(n):
            if matrice[i][j] == 0 or matrice[i][j] == 3:
                if i>0 and matrice[i-1][j+1] == 1:
                    matrice[i-1][j+1] = 3
                if matrice[i][j+1] == 1:
                    matrice[i][j+1] = 3
                if i<n-1 and matrice[i+1][j+1] == 1:
                    matrice[i+1][j+1] = 3
    return matrice

def ovest(n,m,matrice):
    for j in range(m-1,0,-1):
        for i in range(n):
            if matrice[i][j] == 0 or matrice[i][j] == 3:
                if i>0 and matrice[i-1][j-1] == 1:
                    matrice[i-1][j-1] = 3
                if matrice[i][j-1] == 1:
                    matrice[i][j-1] = 3
                if i<n-1 and matrice[i+1][j-1] == 1:
                    matrice[i+1][j-1] = 3
    return matrice

def espandi_rogo(dir,n,m,matrice):
    if dir == "sud":
        sud(n,m,matrice)
    if dir == "nord":
        nord(n,m,matrice)
    if dir == "est":
        est(n,m,matrice)
    if dir == "ovest":
        ovest(n,m,matrice)
    if dir == "sud-est":
        sud(n,m,matrice)
        est(n,m,matrice)
    if dir =="sud-ovest":
        sud(n,m,matrice)
        ovest(n,m,matrice)
    if dir =="nord-est":
        nord(n,m,matrice)
        est(n,m,matrice)
    if dir =="nord-ovest":
        nord(n,m,matrice)
        ovest(n,m,matrice)
    return matrice

# direzioni=["sud", "nord", "est", "ovest", "sud-est", "sud-ovest","nord-est", "nord-ovest"]
# dir=input("Inserisci una direzione: ")
# while dir not in direzioni:
#     print("Direzione non valida, riprova: ")
# n=int(input("Inserisci il numero di righe: "))
# m=int(input("Inserisci il numero di colonne: "))
# matrice = []
# for i in range(n):
#     riga = []
#     for j in range(m):
#         a=int(input("Inserisci un valore compreso tra 0 e 2: "))
#         while a<0 or a>2:
#             a=int(input("Valore non valido, riprova: "))
#         riga.append(a)
#     matrice.append(riga)

dir="nord-est"
n=7
m=5
matrice=[[1, 1, 1, 2, 1],
[1, 1, 2, 1, 1],
[1, 0, 1, 1, 1],
[1, 1, 1, 1, 1],
[2, 2, 2, 2, 2],
[1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1]]

nuova_matrice=espandi_rogo(dir,n,m,matrice)
for i in range(n):
    for j in range(m):
        print(matrice[i][j],end=" ")
    print()

