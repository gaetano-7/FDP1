def main():
    estr=riemp()
    gioc=riemp()
    f=gioco(estr,gioc)
    print(f,end="")

def riemp():
    m=[]
    for i in range(10):
        m.append(int(input()))
    return m

def gioco(estr,gioc):
    d=[]
    for i in range(len(gioc)-1):
        c=[]
        if gioc[i] in estr:
            k=1
            c.append(gioc[i])
            while gioc[i+k] in estr:
                c.append(gioc[i+k])
                k+=1
        if len(c)>=2:
            d.append(c)
    l=[]
    for k in range(len(d)):
        l.append(len(d[k]))
    if len(l)==0:
        return 0
    else:
        return max(l)

    

main()
