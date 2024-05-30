def main():
    N=int(input())
    X=int(input())
    mat=riempi_mat(N)
    u=uno(mat,N)
    d=due(mat,N,X)
    print(str(u)+" "+str(d),end="")

def riempi_mat(N):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(2):
            m[i].append(int(input()))
    return m

def uno(mat,N):
    anni=[]
    for i in range(N):
        anni.append(mat[i][1])
    l=0
    for i in range(len(anni)-1):
        c=0
        for j in range(i+1,len(anni)):
            if anni[i]==anni[j]:
                c+=anni[i]
        if c>l:
            l=c
    return l

def due(mat,N,X):
    c=0
    for i in range(N):
        if mat[i][1]==X:
            c+=mat[i][0]
    if c==0:
        return "SI"
    else:
        return "NO"

main()