def main():
    n=int(input())
    div=trova_d(n)
    c=gioco(div)
    if c==1:
        print("SI",end="")
    else:
        print("NO",end="")

def trova_d(n):
    d=[]
    for i in range(1,n+1):
        if n%i==0:
            d.append(i)
    return d

def gioco(div):
    c=0
    l=len(div)
    if l in div:
        c=1
    return c

main()