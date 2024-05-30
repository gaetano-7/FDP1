def main():
    seq=leggi_seq()
    new_seq=elimina(seq)
    c=dispari(new_seq)
    d=controlla(c)
    if len(c)==0 or len(c)==1:
        print("SI",end="")
    else:
        if d==0:
            print("NO",end="")
        elif d==1:
            print("SI",end="")

def leggi_seq():
    l=[]
    n=input()
    while n!=".":
        l.append(int(n))
        n=input()
    return l

def elimina(seq):
    f=[]
    seq.append(".")
    for i in range(len(seq)-1):
        if seq[i]!=seq[i+1]:
            f.append(seq[i])
    return f
            

def dispari(seq):
    dis=[]
    pari=[]
    for i in range(len(seq)):
        if i%2==0:
            pari.append(seq[i])
        else:
            dis.append(seq[i])
    return dis
    
def controlla(dis):
    c=0
    for j in range(len(dis)-1):
        if dis[j+1]>dis[j]:
            c=1
        else:
            c=0
    return c


main()