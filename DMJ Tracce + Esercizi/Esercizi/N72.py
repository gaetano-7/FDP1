risp=[]
for i in range(20):
    s=str(input())
    risp.append(s)

stamp=[]

for i in range(90):
    l=[]
    macola=input()
    voto=0
    for i in range(20):
        s=str(input())
        l.append(s)
    for i in range(20):
        if l[i]==risp[i]:
            voto+=2
        elif l[i]!="X" and l[i]!=risp[i]:
            voto+=-1
        elif l[i]=="X":
            voto+=0
    stamp.append(macola)
    stamp.append(voto)

for i in range(0,len(stamp)-1,+2):
    print(stamp[i],stamp[i+1])