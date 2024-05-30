N=(input())
L=[]
for i in N:
    L.append(i)
min=""
max=""
L.sort()
for i in L:
    min+=i
L.reverse()
for i in L:
    max+=i
    
print(int(max)-int(min),end="")