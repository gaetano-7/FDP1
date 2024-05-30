def main():
    N=int(input())
    L=riempi_lista(N)
    if ric(L,0):
        print("SI",end="")
    else:
        print("NO",end="")
    
def riempi_lista(N):
    L=[]
    for i in range(N):
        L.append(int(input()))
    return L

def ric(L,i):
    if i>(len(L)//2-1):
        return True
    if L[i]==L[i+len(L)//2]:
        return ric(L,i+1)
    return False

main()