x=int(input())
l=[]
for i in range(x):
    n=int(input())
    l.append(n)
strett=False
pari=[]
dispari=[]
for i in range(len(l)):
    if i%2==0:
        pari.append(l[i])
    else:
        dispari.append(l[i])
            
for i in range(len(pari)-1):
    if pari[i]<pari[i+1]:
        strett=True
        
tutti=False
for i in range(len(dispari)):
    if dispari[i]%2==0:
        tutti=True
        

if strett==True and tutti==False:
    print("SI",end="")
elif x==0:
    print("SI",end="")
else:
    print("NO",end="")
    