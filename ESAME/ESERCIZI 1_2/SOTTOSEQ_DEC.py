def main():
    seq=leggi_seq()
    al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','t','v','w','x','y','z']
    gioco(al,seq)

def leggi_seq():
    m=[]
    n=input()
    while n!="*":
        m.append(str(n))
        n=input()
    return m

def gioco(al,seq):
    e=[]
    f=[]
    for i in range(len(seq)-1):
        pos=al.index(seq[i])
        if seq[i+1] in al[:pos+1]:
            f.append(seq[i])
            e.append(seq[i+1])
            if seq[i+1] not in al[:pos]:
                break
    cont=0
    if len(e)>0 and len(f)>0:
        pri=al.index(e[len(e)-1])
        ult=al.index(f[0])
        for i in range(pri+1,ult):
            cont+=1
    
    print(cont,end="")



main()

