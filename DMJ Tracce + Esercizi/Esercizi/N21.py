A=input()
C=True
while A != ".":
    if A.isalpha()==True:
        C=False
    A=input()
    
if C:
    print("SI",end="")
else :
    print("NO",end="")