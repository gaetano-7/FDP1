def main():
    N=int(input())
    mat=riempi_mat(N)
    if ric(mat,N,0,N-1):
        print("SI",end="")
    else:
        print("NO",end="")
    
def riempi_mat(N):
    mat=[]
    for i in range(N):
        mat.append([])
        for j in range(N):
            mat[i].append(int(input()))
    return mat

def ric(mat,N,i,j):
    if i>=N-1 and j<=0:
        return True
    ris=0
    for k in range(0,N-i):
        ris+=mat[k][i]
    for k in range(i,N):
        ris+=mat[j][k]
    ris-=mat[j][i]
    if ris%mat[j][i]==0:
        return ric(mat,N,i+1,j-1)
    return False
main()