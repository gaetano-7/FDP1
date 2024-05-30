def main():
    N=int(input())
    L=leggi_lista(N)
    s=convert(L)
    print(ric(s,len(s)-1),end="")
              
def leggi_lista(N):
    L=[]
    for i in range(N):
        L.append(int(input()))
    return L

def convert(L):
    s=""
    for i in range(len(L)):
        s+=str(L[i])
    return s

def ric(s,i):
    if i==0:
        return s[0]
    return s[i]+ric(s,i-1)

main()