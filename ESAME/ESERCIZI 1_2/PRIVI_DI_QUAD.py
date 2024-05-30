def main():
    A=int(input())
    B=int(input())
    q=quadrati(A)
    if len(q)==B or B>7:
        print("SI",end="")
    else:
        print("NO",end="")

def quadrati(A):
    l=[]
    for i in range(1,A):
        c=str(i**(1/2))
        if len(c)<=3:
            l.append(i)
    if 1 in l:
        l.remove(1)

    privi=[]
    for x in range(1,A):
        b=0
        for y in range(len(l)):
            if x%l[y]!=0:
                b+=1
        if b==len(l):
            privi.append(x)
    return privi


main()