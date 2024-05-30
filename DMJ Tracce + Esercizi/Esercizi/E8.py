N=int(input())

mat=[]
for i in range(N):
    mat.append([])
    for j in range(N):
        mat[i].append(int(input()))

lix=True
for i in range(N):
    if mat[i].count(mat[i][0])!=1:
        lix=False

mat2=[]
for i in range(N):
    mat2.append([])
    for j in range(N):
        mat2[i].append(mat[j][i])

lix2=True
for i in range(N):
    if mat2[i].count(mat2[i][0])!=1:
        lix2=False


if lix==False and lix2==False:
    print("NO",end="")
else:
    print("SI",end="")