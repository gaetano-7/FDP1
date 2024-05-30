X=int(input())
mat=[]

for i in range(10):
    mat.append([])
    for j in range(10):
        mat[i].append(0)
        
cont=1
for i in range(10):
    for j in range(10):
        mat[i][j]=cont
        cont+=1
        if cont==X+1:
            cont=1
            
somma=0
for i in range(10):
    for j in range(10):
        if j==10-1-i:
            somma+=mat[i][j]

print(somma,end="")
        
        
