import math
n=int(input())
lix=True

while n!=0:
    calc=math.log(n,2)
    if 2**calc!=n:
        lix=False
    n=int(input())

if lix:
    print("SI",end="")
else:
    print("NO",end="")