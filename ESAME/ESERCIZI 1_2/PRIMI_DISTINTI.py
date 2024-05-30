def main():
    A=int(input())
    B=int(input())
    C=int(input())
    divA=divisori(A)
    divB=divisori(B)
    tut=unisci(divA,divB)
    if len(tut)==C or C<4:
        print("SI",end="")
    else:
        print("NO",end="")
        
def divisori(N):
    div=[]
    for i in range(2,N+1):
        if N%i==0:
            div.append(i)
    primi=[]
    for i in range(len(div)):
        if div[i]>1:
            for j in range(2,div[i]):
                if div[i]%j==0:
                    break
            else:
                primi.append(div[i])
    return primi

def unisci(divA,divB):
    c=[]
    for i in range(len(divA)):
        c.append(divA[i])
    for j in range(len(divB)):
        if divB[j] not in c:
            c.append(divB[j])
    return c

main()