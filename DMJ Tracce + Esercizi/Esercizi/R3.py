def main():
    N=int(input())
    mat=riempi_matrice(N)
    no=non_ric(mat,N)
    si=ric(mat,N,0)
    print(si,end="")
    
def riempi_matrice(N):
    mat=[]
    for i in range(N):
        mat.append([])
        for j in range(N):
            mat[i].append(int(input()))
    return mat

def non_ric(mat,N):
    somma=0
    for i in range(N):
        somma+=mat[i][N-1-i]
    return somma

def ric(mat,N,i):
    somma=0
    if i>(N-1):
        return somma
    somma+=mat[i][N-1-i]
    return somma + ric(mat,N,i+1)
    
    
main()
