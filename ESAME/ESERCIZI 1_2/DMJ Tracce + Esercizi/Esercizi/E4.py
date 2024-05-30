N=int(input())
M=int(input())

mat=[]
for i in range(N):
    mat.append([])
    for j in range(M):
        mat[i].append(int(input()))

cont=M

for i in range(M):
    for j in range(N):
        if mat[j][i]==18:
            cont-=1
            break

somme=[]   
for i in range(N):
    if 0 not in mat[i]:
        somme.append(round(sum(mat[i])/len(mat[i])))
    elif 0 in mat[i]:
        for i in range(len(mat[i])):
            if mat[i][i]!=0:
                somme.append(mat[i][i])

sim=0
for i in range(len(somme)):
    sim=somme[0]
         
print(int(cont),int(sim),end="")