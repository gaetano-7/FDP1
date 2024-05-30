def main():
    N=int(input())
    mat=crea_mat(N)
    r_mat=revers(N,mat)
    col=riempi_seq(N)
    rig=riempi_seq(N)
    rig2=riga(N,mat)
    col2=colo(N,r_mat)
    if col==col2 and rig==rig2:
        print("SI",end="")
    else:
        print("NO",end="")


def crea_mat(N):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(N):
            m[i].append(int(input()))
    return m

def revers(N,mat):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(N):
            m[i].append(mat[j][i])
    return m

def riempi_seq(N):
    s=[]
    for i in range(N):
        s.append(int(input()))
    return s

def riga(N,mat):
    c=[]
    for i in range(N):
        d=0
        for j in range(N):
            if mat[i][j]==1:
                d+=1
        c.append(d)
    return c

def colo(N,r_mat):
    c=[]
    for i in range(N):
        d=0
        for j in range(N):
            if r_mat[i][j]==1:
                d+=1
        c.append(d)
    return c

main()