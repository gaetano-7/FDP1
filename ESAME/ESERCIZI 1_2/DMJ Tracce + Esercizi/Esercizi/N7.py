n=int(input())
bool=False
while n!=5:
    if(n%5==0):
        bool=True
    n=int(input())
    
if(bool):
    print("ALMENO 1",end="")
else:
    print("NESSUNO",end="")