N=int(input())
Ninv=0
Norig=N
while N>0:
    Ninv*=10
    Ninv+= N%10
    N//=10

print(Norig-Ninv,end="")