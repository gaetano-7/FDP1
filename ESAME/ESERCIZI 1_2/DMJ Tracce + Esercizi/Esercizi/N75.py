s=str(input())
frase=[]
for i in range(len(s)):
    frase.append(s[i])
    
alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lix=True
for i in range(len(alfabeto)):
    if alfabeto[i] not in frase:
        lix=False
    
if lix==False:
    print("NO",end="")
elif lix==True:
    print("SI",end="")
