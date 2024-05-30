x=int(input())
n=int(input())
l=""
for i in range(n):
    y=int(input())
    if y%2==0 and y<x:
        l+=str(y)
    
print(l,end="")