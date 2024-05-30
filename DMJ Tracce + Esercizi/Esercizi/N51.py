l1=[]
l2=[]
s1=str(input())
while s1!=".":
    l1.append(s1)
    s1=str(input())

s2=str(input())
while s2!=".":
    l2.append(s2)
    s2=str(input())

disgiunte=True
elem=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            disgiunte=False
            elem.append(l1[i])

if disgiunte==True:
    print("DISGIUNTE",end="")
elif disgiunte==False:
    print(elem[0],end="")
