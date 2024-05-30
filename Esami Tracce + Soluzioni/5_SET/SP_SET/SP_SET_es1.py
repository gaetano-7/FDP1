from random import randint
def main():
    N=3
    #int(input())
    r_min=1
    #int(input())
    r_max=2
    #int(input())
    c_min=1
    #int(input())
    c_max=2
    #int(input())
    tot_min=3
    #int(input())
    tot_max=7
    #int(input())
    t=10
    #int(input())
    mat=riempi_e_controlla_tot(N,tot_min,tot_max)
    if len(mat)>0:
        righe=controlla_righe(mat,N,r_min,r_max)
        colonne=controlla_colonna(mat,N,c_min,c_max)
        for i in range(N):
            print(mat[i])
        print(righe)
        print(colonne)
    
    
def riempi_e_controlla_tot(N,tot_min,tot_max):
    tot=0
    qr=[]
    for i in range(N):
        qr.append([])
        for j in range(N):
            x=randint(0,1)
            if x==1:
                qr[i].append("*")
            else:
                qr[i].append("")
    for i in range(N):
        for j in range(N):
            if qr[i][j]=="*":
                tot+=1
    if tot>=tot_min and tot<=tot_max:
        return qr
    else:
        return []
    
def controlla_righe(mat,N,r_min,r_max):
    for i in range(N):
        tot_riga=0
        for j in range(N):
            if mat[i][j]=='*':
                tot_riga+=1
        if tot_riga>=r_min and tot_riga<=r_max:
            return True
        else:
            return False
        
def controlla_colonna(mat,N,c_min,c_max):
    for j in range(N):
        tot_colonna=0
        for i in range(N):
            if mat[i][j]==" ":
                tot_colonna+=1
        if tot_colonna>=c_min and tot_colonna<=c_max:
            return True
        else:
            return False

main()