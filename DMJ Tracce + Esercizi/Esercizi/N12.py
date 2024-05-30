N=int(input())
primo=True
for i in range(2,N):
    if N%i==0:
        primo=False
if primo:
    print("SI",end="")
else:
    print("NO",end="")