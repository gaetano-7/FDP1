s=str(input())
L=[]
for i in s:
    L.append(i)
pare=0
pars=False
for i in L:
    if i=="(":
        pare+=1
    elif i==")":
        pare+=-1
if pare<0:
    pars=True
    
if pare==0 and not pars:
    print("ok1")
else:
    print("no1")

lix=False
for i in range(len(L)-1):
    if L[i]=="(" and L[i+1]==")":
        lix=True
    

if not lix:
    print("ok2")
else:
    print("no2")