M=int(input())
N=int(input())
x=0
y=0
l=2

while M!=0 and M!=l:
    if M%l==0:
        y=1
        break
    l+=1

l=2

while N!=0 and N!=l:
    if N%l==0:
        y=1
        break
    l+=1
    
diff=abs(N-M)

if x!=0 or y!=0:
    print("non entrambi primi",end="")
elif diff!=2:
    print("non gemelli",end="")
else:
    print("gemelli",end="")
       
