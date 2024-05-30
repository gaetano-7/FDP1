s=str(input())
n=int(input())
elenco=[]
for i in range(n):
    x=str(input())
    elenco.append(x)

lix=False
for i in range(len(elenco)):
    for j in range(len(elenco)-1):
        if elenco[i]+elenco[j]==s:
            lix=True

if lix==True:
    print("OK",end="")
else:
    xn=(max(elenco)+min(elenco))
    print(xn,end="")