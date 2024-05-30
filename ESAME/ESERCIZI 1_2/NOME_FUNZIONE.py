def main():
    seq=stringa()
    d=gioco(seq)
    if d==0:
        print("SI",end="")
    if d==1:
        print("NO",end="")

def stringa():
    s=[]
    n=input()
    while n!=":":
        s.append(str(n))
        n=input()
    return s

def gioco(seq):
    c=0
    if seq[0]!="def":
        c=1
    if seq[1].isidentifier()==False:
        c=1
    if seq[2]!="(":
        c=1
    if len(seq[3:len(seq)-1])>0:
        vir=0
        cra=0
        for i in range(3,len(seq)-1):
            if seq[i]!=",":
                cra+=1
                if seq[i].isidentifier()==False:
                    c=1
            else:
                vir+=1
        if cra-1!=vir:
            c=1
    if seq[len(seq)-1]!=")":
        c=1
    return c
    
    




main()