n=int(input())
mat=[]
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append(int(input()))
sommacroce=0

#ORIZZONTALE
for i in range(len(mat)//2,len(mat)//2+1):
    for j in range(0,len(mat)):
        sommacroce+=mat[i][j]
        
#VERTICALE
for i in range(0,len(mat)):
    for j in range(len(mat)//2,len(mat)//2+1):
        sommacroce+=mat[i][j]
        
#CENTRALE
for i in range (len(mat)//2,len(mat)//2+1):
    for j in range(len(mat)//2,len(mat)//2+1):
        sommacroce-=mat[i][j]

somma=0
for i in range(n):
    for j in range(n):
        somma+=mat[i][j]

sommaestern=somma-sommacroce

if sommacroce>sommaestern:
    print("OK",end="")
else:
    print("NO",end="")