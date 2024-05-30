def main():
    N=int(input())
    divis=divisori(N)
    if len(divis) in divis:
        print("SI",end="")
    else:
        print("NO",end="")
    
def divisori(N):
    L=[]
    for i in range(1,N+1):
        if N%i==0:
            L.append(i)
    return L

main()