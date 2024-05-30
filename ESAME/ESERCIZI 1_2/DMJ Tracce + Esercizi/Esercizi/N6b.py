sconti=[10,15,25]
bigl=float(input())
cond=int(input())

if cond==0:
    print(bigl,end="")
elif cond==1:
    print(round(bigl-(bigl*10/100),3),end="")
elif cond==2:
    print(round(bigl-(bigl*15/100),3),end="")
elif cond==3:
    print(round(bigl-(bigl*20/100),3),end="")
