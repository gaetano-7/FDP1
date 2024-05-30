def main():
    N=5
    mat=[["  "," 5","C "," 4","  "],
         ["A3","B1","  ","  ","D4"],
         ["E5","  ","  ","D ","A "],
         ["  ","  ","  "," 1","B "],
         ["D1","  ","  ","  ","C "]]
    alfa=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a=lettere(N,alfa)
    n=numeri(N)
    a_r=rig(N,mat,0)
    n_r=rig(N,mat,1)
    a_c=col(N,mat,0)
    n_c=col(N,mat,1)
    gioco(N,mat,a,a_r,a_c,n_r,n_c)

def lettere(N,alfa):
    a=[]
    for i in range(N):
        a.append(alfa[i])
    return a

def numeri(N):
    l=[]
    for i in range(1,N+1):
        l.append(i)
    return l

def printa(N,mat):
    for i in range(N):
        print(mat[i])

def rig(N,mat,k):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(N):
            m[i].append(mat[i][j][k])
    return m

def col(N,mat,k):
    m=[]
    for i in range(N):
        m.append([])
        for j in range(N):
            m[i].append(mat[j][i][k])
    return m

def controllo(N,mat):
    c=1
    for i in range(N):
        for j in range(N):
            for k in range(2):
                if mat[i][j][k]==" ":
                    c=0
    return c

def gioco(N,mat,a,a_r,a_c,n_r,n_c):
    while controllo(N,mat)==0:
        i=int(input())
        j=int(input())
        car=input()
        if car in a:
            if car not in a_r[i] and car not in a_c[j]:
                mat[i][j]=str(car)+str(mat[i][j][1])
                a_r[i][j]=str(car)
                a_c[j][i]=str(car)
        if car not in a:
            if car not in n_r[i] and car not in n_c[j]:
                mat[i][j]=str(mat[i][j][0])+str(car)
                n_r[i][j]=str(car)
                n_c[j][i]=str(car)
        printa(N,mat)
    
main()