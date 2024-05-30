N=input()
zero=0
for i in N:
    if i=="0":
        zero+=1

if zero==0:
    print("SI",end="")
else:
    print("NO",end="")