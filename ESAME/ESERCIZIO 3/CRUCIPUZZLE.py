def main():
    N=int(input())
    M=int(input())
    mat=crea_mat(N,M)
    K=int(input())
    parole=riempi_seq(K)
    mat2=copia_mat(mat,N,M)  
    orizzontale(mat,N,M,parole,mat2)
    verticale(mat,N,M,parole,mat2)
    diagonale(mat,N,M,mat2,parole)
    g=trova_parola(mat2)
    print(g,end="")

def crea_mat(N,M):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(M):
            m[i].append(str(input()))
    return m

def riempi_seq(K):
    x=[]
    for i in range(K):
        x.append(str(input()))
    return x

def copia_mat(mat,N,M):
    n=[]
    for i in range(N):
        n.append([])
        for j in range(M):
            n[i].append(mat[i][j])
    return  n

def orizzontale(mat,N,M,parole,mat2):
    for i in range(N):
        o=""
        for j in range(M):
            if j==0 or j==1 or j==2:
                o=mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i][j+3]
                for k in range(len(parole)):
                    if o==parole[k]:
                        mat2[i][j]="_"
                        mat2[i][j+1]="_"
                        mat2[i][j+2]="_"
                        mat2[i][j+3]="_"

            if j==0 or j==1 and len(mat[i])>4:
                o=mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i][j+3]+mat[i][j+4]
                for k in range(len(parole)):
                    if o==parole[k]:
                        mat2[i][j]="_"
                        mat2[i][j+1]="_"
                        mat2[i][j+2]="_"
                        mat2[i][j+3]="_"
                        mat2[i][j+4]="_"

            if j==0:
                o=mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i][j+3]+mat[i][j+4]+mat[i][j+5]
                for k in range(len(parole)):
                    if o==parole[k]:
                        mat2[i][j]="_"
                        mat2[i][j+1]="_"
                        mat2[i][j+2]="_"
                        mat2[i][j+3]="_"
                        mat2[i][j+4]="_"
                        mat2[i][j+5]="_"
            
            
def verticale(mat,N,M,parole,mat2):
    mat_r=[]
    for i in range(N):
        mat_r.append([])  
        for j in range(N):
            mat_r[i].append(mat[j][i])
    for i in range(N):
        o=""
        for j in range(M):
            if j==0 or j==1 or j==2:
                o=mat_r[i][j]+mat_r[i][j+1]+mat_r[i][j+2]+mat_r[i][j+3]
                for k in range(len(parole)):
                    if o==parole[k]:
                        mat2[j][i]="_"
                        mat2[j+1][i]="_"
                        mat2[j+2][i]="_"
                        mat2[j+3][i]="_"


            if j==0 or j==1 and len(mat_r[i])>4:
                o=mat_r[i][j]+mat_r[i][j+1]+mat_r[i][j+2]+mat_r[i][j+3]+mat_r[i][j+4]
                for k in range(len(parole)):
                    if o==parole[k]:
                        mat2[j][i]="_"
                        mat2[j+1][i]="_"
                        mat2[j+2][i]="_"
                        mat2[j+3][i]="_"
                        mat2[j+4][i]="_"


            if j==0:
                o=mat_r[i][j]+mat_r[i][j+1]+mat_r[i][j+2]+mat_r[i][j+3]+mat_r[i][j+4]+mat_r[i][j+5]
                for k in range(len(parole)):
                    if o==parole[k]:
                        mat2[j][i]="_"
                        mat2[j+1][i]="_"
                        mat2[j+2][i]="_"
                        mat2[j+3][i]="_"
                        mat2[j+4][i]="_"
                        mat2[j+5][i]="_"

def diagonale(mat,N,M,mat2,parole):
    diag=[]
    for i in range (len(mat[0])+len(mat) - 1):
        diag.append([])

    for i in range(len(mat[0])):
        for j in range(len(mat)):
            diag[i-j-(-len(mat)+1)].append(str(i)+str(j))
    d=[]
    for i in range(len(diag)):
        if len(diag[i])>=4:
            d.append(diag[i])

    for i in range(len(d)):
        o=""
        for j in range(len(d[i])):
            for k in range(len(parole)):
                if j==0 and len(d[i])==4:
                    o=mat[int(d[i][j][0])][int(d[i][j][1])] + mat[int(d[i][j+1][0])][int(d[i][j+1][1])] + mat[int(d[i][j+2][0])][int(d[i][j+2][1])] + mat[int(d[i][j+3][0])][int(d[i][j+3][1])] 
                    if o==parole[k]:
                        mat2[int(d[i][j][0])][int(d[i][j][1])]="_"
                        mat2[int(d[i][j+1][0])][int(d[i][j+1][1])]="_"
                        mat2[int(d[i][j+2][0])][int(d[i][j+2][1])]="_"
                        mat2[int(d[i][j+3][0])][int(d[i][j+3][1])]="_"
                if j==0 and len(d[i])==5:
                    o=mat[int(d[i][j][0])][int(d[i][j][1])] + mat[int(d[i][j+1][0])][int(d[i][j+1][1])] + mat[int(d[i][j+2][0])][int(d[i][j+2][1])] + mat[int(d[i][j+3][0])][int(d[i][j+3][1])] 
                    if o==parole[k]:
                        mat2[int(d[i][j][0])][int(d[i][j][1])]="_"
                        mat2[int(d[i][j+1][0])][int(d[i][j+1][1])]="_"
                        mat2[int(d[i][j+2][0])][int(d[i][j+2][1])]="_"
                        mat2[int(d[i][j+3][0])][int(d[i][j+3][1])]="_"
                if j==1 and len(d[i])==5:
                    o=mat[int(d[i][j][0])][int(d[i][j][1])] + mat[int(d[i][j+1][0])][int(d[i][j+1][1])] + mat[int(d[i][j+2][0])][int(d[i][j+2][1])] + mat[int(d[i][j+3][0])][int(d[i][j+3][1])] 
                    if o==parole[k]:
                        mat2[int(d[i][j][0])][int(d[i][j][1])]="_"
                        mat2[int(d[i][j+1][0])][int(d[i][j+1][1])]="_"
                        mat2[int(d[i][j+2][0])][int(d[i][j+2][1])]="_"
                        mat2[int(d[i][j+3][0])][int(d[i][j+3][1])]="_"
                if j==0 and len(d[i])==6:
                    o=mat[int(d[i][j][0])][int(d[i][j][1])] + mat[int(d[i][j+1][0])][int(d[i][j+1][1])] + mat[int(d[i][j+2][0])][int(d[i][j+2][1])] + mat[int(d[i][j+3][0])][int(d[i][j+3][1])] 
                    if o==parole[k]:
                        print(o)
                        mat2[int(d[i][j][0])][int(d[i][j][1])]="_"
                        mat2[int(d[i][j+1][0])][int(d[i][j+1][1])]="_"
                        mat2[int(d[i][j+2][0])][int(d[i][j+2][1])]="_"
                        mat2[int(d[i][j+3][0])][int(d[i][j+3][1])]="_"
                if j==1 and len(d[i])==6:
                    o=mat[int(d[i][j][0])][int(d[i][j][1])] + mat[int(d[i][j+1][0])][int(d[i][j+1][1])] + mat[int(d[i][j+2][0])][int(d[i][j+2][1])] + mat[int(d[i][j+3][0])][int(d[i][j+3][1])] 
                    if o==parole[k]:
                        print(o)
                        mat2[int(d[i][j][0])][int(d[i][j][1])]="_"
                        mat2[int(d[i][j+1][0])][int(d[i][j+1][1])]="_"
                        mat2[int(d[i][j+2][0])][int(d[i][j+2][1])]="_"
                        mat2[int(d[i][j+3][0])][int(d[i][j+3][1])]="_"
                if j==2 and len(d[i])==6:
                    o=mat[int(d[i][j][0])][int(d[i][j][1])] + mat[int(d[i][j+1][0])][int(d[i][j+1][1])] + mat[int(d[i][j+2][0])][int(d[i][j+2][1])] + mat[int(d[i][j+3][0])][int(d[i][j+3][1])] 
                    if o==parole[k]:
                        print(o)
                        mat2[int(d[i][j][0])][int(d[i][j][1])]="_"
                        mat2[int(d[i][j+1][0])][int(d[i][j+1][1])]="_"
                        mat2[int(d[i][j+2][0])][int(d[i][j+2][1])]="_"
                        mat2[int(d[i][j+3][0])][int(d[i][j+3][1])]="_"

def trova_parola(mat2):
    k=""
    for i in range(len(mat2)):
        for j in range(len(mat2)):
            if mat2[i][j]!="_":
                k+=mat2[i][j]
    return k

main()