def main():
    dir=input()
    N=7
    #int(input())
    M=5
    #int(input())
    mat=[[1,1,1,2,1],
         [1,1,2,1,1],
         [1,0,1,1,1],
         [1,1,1,1,1],
         [1,1,1,1,1],
         [1,1,1,1,1],
         [1,1,1,1,1]]
    nuova_mat=espandi_rogo(dir,N,M,mat)
    for i in range(N):
        print(nuova_mat[i],end="")
        print()

def sud(N,M,mat):
    for i in range(N-1):
        for j in range(M):
            if mat[i][j]==0 or mat[i][j]==3:
                print(str(i)+str(j))
                if j>0 and mat[i+1][j-1]==1:
                    mat[i+1][j-1]=3
                if mat[i+1][j]==1:
                    mat[i+1][j]=3
                if j<M-1 and mat[i+1][j+1]==1:
                    mat[i+1][j+1]=3
    return mat

def nord(N,M,mat):
    for i in range(N-1,0,-1):
        for j in range(M):
            if mat[i][j]==0 or mat[i][j]==3:
                print(str(i)+str(j))
                if j>0 and mat[i-1][j-1]==1:
                    mat[i-1][j-1]=3
                    if mat[i-1][j]!=2:
                        mat[i-1][j]=3
                    if j<M-1 and mat[i-1][j+1]==1:
                        mat[i-1][j+1]=3
    return mat

def est(N,M,mat):
    for j in range(M-1):
        for i in range(N):
            if mat[i][j]==0 or mat[i][j]==3:
                print(str(i)+str(j))
                if i>0 and mat[i-1][j+1]==1:
                    mat[i-1][j+1]=3
                if mat[i][j+1]==1:
                    mat[i][j+1]=3
                if i<M-1 and mat[i+1][j+1]==1:
                    mat[i+1][j+1]=3
    return mat           

def ovest(N,M,mat):
    for j in range(M-1,0,-1):
        for i in range(N):
            if mat[i][j]==0 or mat[i][j]==3:
                print(str(i)+str(j))
                if i>0 and mat[i-1][j-1]==1:
                    mat[i-1][j-1]=3
                if mat[i][j-1]!=2:
                    mat[i][j-1]=3
                if i<M-1 and mat[i+1][j-1]==1:
                    mat[i+1][j-1]=3
    return mat

def espandi_rogo(dir,N,M,mat):
    if dir == "sud":
        sud(N,M,mat)
    if dir == "nord":
        nord(N,M,mat)
    if dir == "est":
        est(N,M,mat)        
    if dir == "ovest":
        ovest(N,M,mat)       
    if dir == "sud-est":
        sud(N,M,mat)
        est(N,M,mat)       
    if dir == "sud-ovest":
        sud(N,M,mat)
        ovest(N,M,mat)
    if dir == "nord-est":
        nord(N,M,mat)
        est(N,M,mat)       
    if dir == "nord-ovest":
        nord(N,M,mat)
        ovest(N,M,mat)         
    return mat

main()
                
    