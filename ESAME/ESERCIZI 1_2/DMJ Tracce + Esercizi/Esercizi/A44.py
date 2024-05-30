n=list(input())
met=[]
met2=[]
for i in range(len(n)//2):
    met.append(int(n[i]))

for i in range(len(n)//2,len(n)):
    met2.append(int(n[i]))

if sum(met)==sum(met2):
    print("FORTUNATO",end="")
else:
    print("SFORTUNATO",end="")
