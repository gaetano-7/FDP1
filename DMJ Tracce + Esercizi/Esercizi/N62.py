K=int(input())
A=[]
for i in range(K):
    n=int(input())
    A.append(n)
N=int(input())
M=int(input())
mat=[]
for i in range(N):
    mat.append([])
    for j in range(M):
        mat[i].append(0)


for j in range(0,M):
    for  i in range((N-1),-1,-1):
        for k in range(len(A)):
            mat[i][j]=A[k]
            
                
print(mat)