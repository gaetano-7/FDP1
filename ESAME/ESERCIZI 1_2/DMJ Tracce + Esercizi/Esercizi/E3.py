l=[]
n=input()
while n!="*":
    l.append(int(n))
    n=input()

sotto=[]
cont=0

for i in range(0,len(l)-1):
    if l[i]==l[i+1]-1:
        sotto.append(l[i])
    else:
        sotto.append("_")

sotto.insert(0,"_")
sotto.append("_")

for i in range(len(sotto)-1):
    if sotto[i]=="_" and sotto[i+1]!="_":
        cont+=1
        
print(cont,end="")
