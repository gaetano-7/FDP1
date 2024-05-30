M=list(str(input()))
bool=True
for i in range(len(M)):
    if M[0].isdigit() or M[i]==" ":
        bool=False
        break
    for i in range(1,len(M)):
        if M[i].isalpha or M[i].isdigit() or M[i]=="_":
            bool=True
        else:
            bool=False

if bool:
    print("SI",end="")
else:
    print("NO",end="")