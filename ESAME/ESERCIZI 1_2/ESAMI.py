def main():
    N=int(input())
    M=int(input())
    mat=riempi(N,M)
    r_mat=revers(mat,N,M)
    gioco(r_mat,mat,N,M)

def riempi(N,M):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(M):
            m[i].append(int(input()))
    return m

def revers(mat,N,M):
    m=[]
    for i in range(M):
        m.append([])
        for j in range(N):
            m[i].append(mat[j][i])
    return m

def gioco(r_mat,mat,N,M):
    exam=M
    for i in range(M):
        if 18 in r_mat[i]:
            exam-=1
    d=1
    for i in range(N):
        if 0 in mat[i]:
            d=0
    if d==1:
        cont=[]
        for j in range(M):
            cont.append(mat[0][j])
        if 0 in cont:
            cont.remove(0)
        media=round(sum(cont)/len(cont))
    elif d==0:
        cont=[]
        for i in range(N):
            if 0 not in mat[i]:
                cont=mat[i]
                break
            else:
                cont=mat[0]
                break
        if 0 in cont:
            cont.remove(0)
        media=round(sum(cont)/len(cont))
    print(str(exam)+" "+str(media),end="")

        



main()