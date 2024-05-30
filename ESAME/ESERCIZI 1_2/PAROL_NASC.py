n1=int(input())
n2=int(input())

seq=[]
s=str(input())
while s!=".":
    seq.append(s)
    s=str(input())

alfab=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


alfab_2=[]
for i in range(4):
    for j in range(len(alfab)):
        alfab_2.append(alfab[j])

new_s=[]
for i in range(len(seq)):
    new_s.append(str("0"))

for i in range(len(seq)):
    if (i+1)%2==0: #PARI
        p=alfab.index(seq[i])-n2
        new_s[i]=alfab_2[p]
    elif (i+1)%2!=0: #DISPARI
        d=alfab.index(seq[i])+n1
        new_s[i]=alfab_2[d]

r=""
for i in range(len(new_s)):
    r+=str(new_s[i])

print(r,end="")
