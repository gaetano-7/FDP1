A=input()
C=False
while A != ".":
    if A.isalpha()==True:
        C=True
    A=input()
    
if C:
    print("SI",end="")
else :
    print("NO",end="")