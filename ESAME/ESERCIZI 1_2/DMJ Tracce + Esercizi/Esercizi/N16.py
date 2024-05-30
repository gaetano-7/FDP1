x=int(input())
zero=""
l=""
n=int(input())
while n!=-1:
    l+=str(n)
    n=int(input())
        
for i in range(x):
    zero+="0"
    
if zero in l:
    print("OK",end="")
else:
    print("NO",end="")