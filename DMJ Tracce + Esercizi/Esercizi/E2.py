def main():
    N=int(input())
    mat=riempi_matrice(N)
    L_col=riempi_lista(N)
    L_rig=riempi_lista(N)
    lilla_col=ric_col(L_col,mat,0,1,N)
    lilla_rig=ric_rig(L_rig,mat,0,1,N)
    print(lilla_col)
    print(lilla_rig)


    if lilla_col==L_col and lilla_rig==L_rig:
        print("SI",end="")
    else:
        print("NO",end="")
    
def riempi_matrice(N):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(N):
            m[i].append(int(input()))
    return m

def riempi_lista(N):
    L=[]
    for i in range(N):
        L.append(int(input()))
    return L

def ric_col(L_col,mat,f,g,N):
    cont=0
    s=[]
    if g>=N+1:
        return s
    else:
        for i in range(N):
            for j in range(f,g):
                if mat[i][j]==1:
                    cont+=1
        s.append(cont)
        return s + ric_col(L_col,mat,f+1,g+1,N)

def ric_rig(L_rig,mat,f,g,N):
    cont=0
    s=[]
    if g>=N+1:
        return s
    else:
        for i in range(f,g):
            for j in range(N):
                if mat[i][j]==1:
                    cont+=1
        s.append(cont)
        return s + ric_rig(L_rig,mat,f+1,g+1,N)

main()
