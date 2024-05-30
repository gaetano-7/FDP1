string=[]
S=int(input())
while (S >= 0):
    string.append(S)
    S=int(input())
    
prec=string[0]
sottoseq=str(string[0])
sottoseqe=[]
for i in range(1,len(string)):
    att=string[i]
    if(att<prec):
        sottoseqe.append(sottoseq)
        sottoseq=str(att)
    elif(prec<=att):
        sottoseq+=str(att)
    if(i==len(string)-1 and sottoseq!=""):
        sottoseqe.append(sottoseq)
        prec=string[i]

            
prec=sottoseqe[0]
risult=prec
for i in range (1,len(sottoseqe)):
    att=sottoseqe[i]
    if(len(att)>len(prec)):
        risult=att
    prec=att


if(len(string)>0):
    print(risult)
    print(len(risult),end="")
else:
    print("Empty",end="")
