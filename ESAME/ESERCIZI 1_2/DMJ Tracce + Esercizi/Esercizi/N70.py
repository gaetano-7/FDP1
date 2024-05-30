L=list(str(input()))
vocali=["a","e","i","o","u"]


for i in range(len(L)):
        if L[i] in vocali:
            L[i]=(L[i]+'f'+L[i])

lis=""
for i in range(len(L)):
    lis+=str(L[i])

lix=list(lis)
meta1=""
meta2=""
for i in range(0,len(lix)//2):
    meta1+=str(lix[i])
for i in range(len(lix)//2,len(lix)):
    meta2+=str(lix[i])
    
print(meta2+meta1,end="")
    

