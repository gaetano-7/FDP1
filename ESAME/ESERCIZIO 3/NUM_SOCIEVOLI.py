def main():
    L=[12496,14288,15472,14536,14264]
    s=ric(L,0)
    print(s)
    
def ric(L,k):
    lix=False
    somma=0
    if k==len(L)-1:
        return lix
    else:
        for i in range(1,L[k]):
            if L[k]%i==0:
                somma+=i
        if somma==L[k+1] or somma==L[0]:
            lix=True
            return lix
    return ric(L,k+1)

main()