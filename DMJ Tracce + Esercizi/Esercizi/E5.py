l=[]
n=input()
while n!="*":
    l.append(str(n))
    n=input()

lett=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

s=[]
si=[]
for i in range(len(l)-1):
    if l[i+1] in lett[:lett.index(l[i])+1]:
        si.append(l[i])
        s.append(l[i+1])
        if l[i+1] not in lett[:lett.index(l[i])]:
            break
        
cont=0
if len(s)>0 and len(si)>0:
    pri=lett.index(s[len(s)-1])
    ult=lett.index(si[0])
    for i in range(pri+1,ult):
        cont+=1
    
print(cont,end="")
