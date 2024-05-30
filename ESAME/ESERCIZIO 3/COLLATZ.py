def main():
    L=riempi_lista()
    N=int(input())
    new_L=ric(N)
    print(controlla(N,L,new_L))
    
def riempi_lista():
    l=[]
    n=int(input())
    while n!=1:
        l.append(n)
        n=int(input())
    l.append(n)
    return l

def ric(N):
    lix=[]
    if N==1:
        return lix
    else:
        if N%2==0:
            Ne=N//2
            lix.append(Ne)
        elif N%2!=0:
            Ne=3*N+1
            lix.append(Ne)
        return lix + ric(Ne)
    
def controlla(N,L,new_L):
    new_L.insert(0,N)
    if new_L==L:
        return True
    else:
        return False

main()