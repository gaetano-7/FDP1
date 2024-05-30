n=int(input())
x=int(input())
cont=0

while x!=-1:
    if x<=n:
        cont+=1
    x=int(input())

print(cont)
#if cont>=n:
 #   print("OK",end="")
#else:
 #   print("NO",end="")