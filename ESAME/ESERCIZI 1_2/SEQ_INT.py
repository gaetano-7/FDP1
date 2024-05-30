def main():
    seq=leggi_seq()
    x=int(input())
    car=str(input())
    f=coppia(seq,x)
    if len(f)>0:
        i=f[0]
        j=f[1]
        gioco(seq,i,j,car)

def leggi_seq():
    l=[]
    n=input()
    while n!=".":
        l.append(int(n))
        n=input()
    return l

def coppia(seq,x):
    l=[]
    for i in range(len(seq)-1):
        if seq[i]+seq[i+1]==x:
            l.append(i)
            l.append(i+1)
            break
    return l
    
def gioco(seq,i,j,car):
    if car=="d":
        a=""
        for k in range(j,len(seq)):
            a+=str(seq[k])
        print(a,end="")
    if car=="s":
        d=""
        for h in range(i,0-1,-1):
            d+=str(seq[h])
        print(d,end="")

main()