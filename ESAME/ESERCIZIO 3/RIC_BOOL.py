def main():
    N=324
    M=8
    new=rotate(N)
    d=ric(new,M,0)
    print(d)

def rotate(N):
    c=str(N)
    l=[]
    l.append(int(c))
    for i in range(1,len(c)-1):
        l.append(int(c[i]+c[i+1]+c[i-1]))
        l.append(int(c[i+1]+c[i-1]+c[i]))
    return l

def ric(new,M,i):
    dd=0
    if i>=len(new):
        return dd
    if new[i]%M==0:
        dd=1
    return dd + ric(new,M,i+1)

main()

