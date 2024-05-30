def main():
    X=int(input())
    N=int(input())
    L=riempi_lista(N)
    print(ric(L,X),end="")
    
def riempi_lista(N):
    L=[]
    for i in range(N):
        L.append(int(input()))
    return L

def ric(L,X):
    if X not in L:
        return 0
    C=L.count(X)
    for i in range(len(L)):
        if L[i]==X:
            L[i]=0
    return C + ric(L,C)

main()