seq=["def","pari","(","n",",","m",",","mat",")"]
vir=0
stri=0
if len(seq[3:(len(seq)-1)])>1:
    for i in range(3,len(seq)-1):
        if seq[i]==",":
            vir+=1
    for i in range(3,len(seq)-1):
        if seq[i]!=",":
            stri+=1   
print(stri)
print(vir)
if (stri-1)==vir:
    print("SI",end="")
else:
    print("NO",end="")