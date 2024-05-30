L=[]
for i in range(10):
    n=int(input())
    L.append(n)
    
min=[]
for i in (L):
    if i>50:
        min.append(i)
    elif i<-50:
        min.append(i)
if len(min)==0:
    print("VUOTO1",end="")

for i in min:
    if len(min)>0:
        print(i,end="")
print()
valori=[]
for i in L:
    if i>=-50 and i<=50:
        valori.append(i)


if len(valori)==0:
    print("VUOTO2",end="")
else:
    print(round(sum(valori)/len(valori),6))