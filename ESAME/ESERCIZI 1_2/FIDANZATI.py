def main():
    a=int(input())
    b=int(input())
    a=a-1
    b=b+1
    estr=crea_intervallo(a,b)
    p=fidanzati(estr,a,b)
    p2=fidanzati2(p)
    if p2>0:
        print("SI",end="")
    else:
        print("NO",end="")

def crea_intervallo(a,b):
    m=[]
    for i in range(a,b+1):
        m.append(i)
    return m

def fidanzati(estr,a,b):
    primi=[]
    for i in range(len(estr)):
        p=0
        for j in range(2,estr[i]+1):
            if estr[i]%j==0:
                if j!=1 and j!=estr[i]:
                    p+=j
        if p>a and p<b:
            primi.append(p)
    return primi

def fidanzati2(primi):
    cont=0
    for i in range(len(primi)):
        p=0
        for j in range(2,primi[i]+1): 
            if primi[i]%j==0:
                if j!=1 and j!=primi[i]:
                    p+=j
        if p in primi:
            new=primi.index(p)
            p2=0
            for k in range(2,primi[new]+1):
                if primi[new]%k==0:
                    if k!=1 and k!=primi[new]:
                        p2+=k
            if primi[i]==p2 and p==primi[new]:
                cont+=1
    return cont

main()