n=int(input())
l=[]
x="*"
for i in range(n):
    l.append(x)
    x+="*"
    x+="*"
somm=[]
sommu=0
for x in l:
    somm.append(len(x))
    sommu+=len(x)
maxi=max(somm)

print((sommu*2)-maxi)