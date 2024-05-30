M_giudici=int(input())
N_cantanti=int(input())
mat=[]
for i in range(M_giudici):
    mat.append([])
    for j in range(N_cantanti):
        mat[i].append(int(input()))
        
giudi_ind=[]
giudi_vot=[]
for i in range(M_giudici):
    cont=0
    for j in range(N_cantanti):
        if mat[i][j]>5:
            cont+=1
    giudi_ind.append(str(i))
    giudi_vot.append(str(cont))

maxi=str(max(giudi_vot))
maxi_vot=[]
for i in range(len(giudi_vot)):
    if giudi_vot[i]==maxi:
        maxi_vot.append(i)
giud_max=max(maxi_vot)



cant_ind=[]
cant_vot=[]
for j in range(N_cantanti):
    cont=0
    for i in range(M_giudici):
        if mat[i][j]>=0:
            cont+=mat[i][j]
    cant_ind.append(str(j))
    cant_vot.append(str(cont))

mini=str(min(cant_vot))
mini_vot=[]
for i in range(len(cant_vot)):
    if cant_vot[i]==mini:
        mini_vot.append(i)

cant_min=max(mini_vot)

print(giud_max,cant_min)

