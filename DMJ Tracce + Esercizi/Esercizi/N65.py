peso=[]
for i in range(0,8):
    n=int(input())
    peso.append(n)

mat=[]
for i in range(70):
    mat.append([])
    for j in range(9):
        mat[i].append(input())

soglia=int(input())
voti=[]
for i in range(70):
    voti.append([])
    voti[i].append(mat[i][0])
    voti[i].append(int(mat[i][1])*peso[0]+int(mat[i][2])*peso[1]+int(mat[i][3])*peso[2]+int(mat[i][4])*peso[3]+int(mat[i][5])*peso[4]+int(mat[i][6])*peso[5]+int(mat[i][7])*peso[6]+int(mat[i][8])*peso[7])
sogl=[]     
for i in range(len(voti)):
    if voti[i][1]>=soglia:
        sogl.append(voti[i])
mini=""
maxi=""
numi=[]
for i in range(len(sogl)):
    numi.append(sogl[i][1])

maxi_n=max(numi)
mini_n=min(numi)

for i in range(len(sogl)):
    if maxi_n==sogl[i][1]:
        maxi=sogl[i][0]
    elif mini_n==sogl[i][1]:
        mini=sogl[i][0]

numeri=[]   
for i in range(len(sogl)):
    numeri.append(sogl[i][1])
    for j in range(len(sogl)):
        print(sogl[i][j],end=' ')
    print()

print(len(sogl),maxi,mini,end="")
