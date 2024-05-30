def main():
    s=str(input())
    N=7
    M=5
    mat=[[1,1,1,2,1],
         [1,1,2,1,1],
         [1,0,1,1,1],
         [1,1,1,1,1],
         [2,2,2,2,2],
         [1,1,1,1,1],
         [1,1,1,1,1]]
    gioco(s,mat,N,M)
    for i in range(N):
        print(mat[i])
    
def sud(mat,N,M):
    for i in range(N):
        for j in range(M):
            if mat[i][j]==0 or mat[i][j]==3:
                if j==0 and i!=N-1:
                    if mat[i+1][j]==1:
                        mat[i+1][j]=3
                    if mat[i+1][j+1]==1:
                        mat[i+1][j+1]=3
                if j==M-1 and i!=N-1:
                    if mat[i+1][j]==1:
                        mat[i+1][j]=3
                    if mat[i+1][j-1]==1:
                        mat[i+1][j-1]=3
                if j!=0 and j!=M-1 and i!=N-1:
                    if mat[i+1][j]==1:
                        mat[i+1][j]=3
                    if mat[i+1][j-1]==1:
                        mat[i+1][j-1]=3
                    if mat[i+1][j+1]==1:
                        mat[i+1][j+1]=3

def nord(mat,N,M):
    for i in range(N-1,0,-1):
        for j in range(M):
            if mat[i][j]==0 or mat[i][j]==3:
                if j==0 and i!=0:
                    if mat[i-1][j]==1: 
                        mat[i-1][j]=3
                    if mat[i-1][j+1]==1:
                        mat[i-1][j+1]=3
                if j==M-1 and i!=0:
                    if mat[i-1][j]==1:
                        mat[i-1][j]=3
                    if mat[i-1][j-1]==1:
                        mat[i-1][j-1]=3
                if j!=0 and j!=M-1 and i!=N-1:
                    if mat[i-1][j]==1: 
                        mat[i-1][j]=3
                    if mat[i-1][j-1]==1:
                        mat[i-1][j-1]=3
                    if mat[i-1][j+1]==1:
                        mat[i-1][j+1]=3

def est(mat,N,M):
    for j in range(M-1):
        for i in range(N):
            if mat[i][j]==0 or mat[i][j]==3:
                if i==0 and j!=M-1:
                    if mat[i][j+1]==1:
                        mat[i][j+1]=3
                    if mat[i+1][j+1]==1:
                        mat[i+1][j+1]=3
                if i==N-1 and j!=M-1:
                    if  mat[i-1][j+1]==1:
                        mat[i-1][j+1]=3
                    if mat[i][j+1]==1:
                        mat[i][j+1]=3
                if i!=0 and i!=N-1 and j!=M-1:
                    if mat[i][j+1]==1:
                        mat[i][j+1]=3
                    if mat[i-1][j+1]==1:
                        mat[i-1][j+1]=3
                    if mat[i+1][j+1]==1:
                        mat[i+1][j+1]=3

def ovest(mat,N,M):
    for j in range(M-1,0,-1):
        for i in range(N):
            if mat[i][j]==0 or mat[i][j]==3:
                if i==0 and j!=0:
                    if mat[i][j-1]==1:
                        mat[i][j-1]=3
                    if mat[i+1][j-1]==1:
                        mat[i+1][j-1]=3
                if i==N-1 and j!=0:
                    if mat[i-1][j-1]==1:
                        mat[i-1][j-1]=3
                    if mat[i][j-1]==1:
                        mat[i][j-1]=3
                if i!=0 and i!=N-1 and j!=0:
                    if mat[i][j-1]==1:
                        mat[i][j-1]=3
                    if mat[i-1][j-1]==1:
                        mat[i-1][j-1]=3
                    if mat[i+1][j-1]==1:
                        mat[i+1][j-1]=3

def gioco(vento,mat,N,M):
    if vento=="sud":
        sud(mat,N,M)
    if vento=="nord":
        nord(mat,N,M)
    if vento=="est":
        est(mat,N,M)
    if vento=="ovest":
        ovest(mat,N,M)
    if vento=="sud-est":
        sud(mat,N,M)
        est(mat,N,M)
    if vento=="sud-ovest":
        sud(mat,N,M)
        ovest(mat,N,M)
    if vento=="nord-est":
        nord(mat,N,M)
        est(mat,N,M)
    if vento=="nord-ovest":
        nord(mat,N,M)
        ovest(mat,N,M)
    
main()