def main():
    A=int(input())
    B=int(input())
    C=int(input())
    D=int(input())
    potenze=prendi_potenze(0)
    l=numero_amico(potenze,A,B)
    f=controlla(l,C,D)
    if f==1:
        print("SI",end="")
    else:
        print("NO",end="")

def prendi_potenze(i):
    m=[]
    if i>=11:
        return m
    m.append(2**i)
    return m + prendi_potenze(i+1)

def numero_amico(potenze,A,B):
    m=[]
    for i in range(A,B+1):
        for j in range(len(potenze)):
            if i==1+potenze[j]:
                m.append(i)
    return m
    
def controlla(l,C,D):
    inter=[]
    for j in range(C,D+1):
        inter.append(j)
    c=0
    for i in range(len(l)):
        if l[i] in inter:
            c=1
        else:
            c=0
    return c
            
main()