num=int(input())
ciclo=str(num)
risp=""
cont=1
if len(ciclo)==1:
    i=0
else:
    for i in range(1,len(str(num))):
        if str(ciclo[i])==str(ciclo[i-1]):
            cont+=1
        else:
            risp+=str(cont)+str(ciclo[i-1])
            cont=1
risp+=str(cont)+str(ciclo[i])
print(risp,len(risp),end="")
