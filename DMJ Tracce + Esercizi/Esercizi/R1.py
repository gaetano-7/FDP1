def main():
    N=int(input())
    print(ric(N),end="")
    
def ric(N):
    if N==0:
        return 2
    return 3*(N+1)*ric(N-1)

main()