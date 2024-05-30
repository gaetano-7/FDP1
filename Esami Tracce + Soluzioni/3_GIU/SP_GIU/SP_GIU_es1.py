def main():
    N=int(input())
    SP=riempi_seq(N)
    SC=riempi_seq2()
    ma=max(SP)
    richieste(SP,SC,0,ma)
    
    
    
def riempi_seq(N):
    s=[]
    for i in range(N):
        x=int(input())
        s.append(x)
    return s

def riempi_seq2():
    l=[]
    x=int(input())
    while x!="*":
        l.append(int(x))
        x=input()
    return l
    
def richieste(SP,SC,i,ma):
    for d in range(len(SC)):
        if SC[d] in SP:
            print(SC[d])
            SP.remove(SC[d])
    for i in range(len(SP)):
        for j in range(len(SP)):
            if i!=j:
                if SP[i]+SP[j]==SC[2]:
                    print(SP[i],SP[j])
                    SP.remove(SP[i])
                    SP.remove(SP[j])
                    break
                else:
                    print("NO")
        break
    return richieste

main()