L=[]
for i in range(10):
    n=input()
    L.append(n)
vocali=["a","e","i","o","u"]
contvoc=[]
for i in range(len(L)):
    if L[i] in vocali:
        if L[i] not in vocali:
            contvoc.append(L[i])

if len(contvoc)>1:
   print("ERRORE",end="")
else:
   print("ERRORE",end="")

