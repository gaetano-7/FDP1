N=int(input())
X=int(input())

mat=[]

for i in range(N):
    mat.append([])
    for j in range(2):
        mat[i].append(int(input()))

anni=[]
for i in range(N):
    anni.append(mat[i][1])

s=[]
for i in range(len(anni)):
    s.append((anni.count(anni[i])))
    
nut=s.index(max(s))

lix=True
for i in range(N):
    if mat[i][1]==X:
        if mat[i][0]!=0:
            lix=False
            break
        else:
            lix=True

if lix==True:
    print(anni[nut],"SI",end="")
else:
    print(anni[nut],"NO",end="")