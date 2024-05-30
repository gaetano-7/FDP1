def collatz(L,i):
    if len(L) == 0:
        return False
    if i == len(L)-1:
        if L[i]==1:
            return True
        else:
            return False
    else:
        x=0
        if L[i]%2==0:
            x=L[i]//2
        else:
            x=L[i]*3+1
        if L[i+1]!=x:
            return False
        return collatz(L,i+1)

L=[10, 5, 16, 8, 4, 2, 45]
#L=[11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
#L=[11,34,17,52,26,13,40,20,10,5,16,8,4,2]
print(collatz(L,0))

