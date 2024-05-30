n=int(input())
l=[]
while n!=-50:
    l.append(n)
    n=int(input())

if len(l)>0:
    media=sum(l)//len(l)
    magg=[]
    for i in range(len(l)):
        if l[i]>=media:
            magg.append(l[i])

if len(l)==0:
    print("VUOTA",end="")
else:
    print(min(magg),end="")


