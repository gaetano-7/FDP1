seq=[]
s=input()
while s!=":":
    seq.append(s)
    s=input()

lix=False
for i in range(len(seq)):
    if seq[0]=="def":              
        lix=True          #la prima parola deve essere ==def
    else:
        print("NO",end="")
        exit()
    
    if seq[1].isidentifier():
        lix=True
    else:
        print("NO",end="")
        exit()

vir=0
stri=0
if len(seq[3:(len(seq)-1)])>0:
    for i in range(3,len(seq)-1):
        if seq[i]!=",":
            if seq[i].isidentifier():
                lix=True
            else:
                print("NO",end="")
                exit()

if len(seq[3:(len(seq)-1)])>1:
    for i in range(3,len(seq)-1):
        if seq[i]==",":
            vir+=1
    for i in range(3,len(seq)-1):
        if seq[i]!=",":
            stri+=1   
    if (stri-1)==vir:
        lix=True
    else:
        print("NO",end="")
        exit()
        
if lix==True:
    print("SI",end="")
    