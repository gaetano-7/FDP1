def main():
    A=int(input())
    B=int(input())
    print(ric(A,B),end="")  
    
def ric(A,B):
    r=A%B
    if r==0:
        return B
    return ric(B,r)

main()