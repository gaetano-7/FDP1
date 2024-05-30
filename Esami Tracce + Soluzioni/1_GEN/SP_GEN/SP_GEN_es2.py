N=input()
M=int(input())

rotazioni=[]
rotazioni.append(int(N))

for i in range(1,len(N)):
    rotazioni.append(int(N[i]+N[i+1]+N[i-1]))
    rotazioni.append(int(N[i+1]+N[i-1]+N[i]))
    break

lix=False
for i in range(len(rotazioni)):
    if rotazioni[i]%M==0:
        lix=True

print(rotazioni)  
print(lix,end="")
    
    
    
   
