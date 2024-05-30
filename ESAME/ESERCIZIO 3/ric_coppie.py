def main():
    A=int(input())
    B=int(input())
    C=int(input())
    D=int(input())
    ric(A,B,C,D,0,1)
    
def ric(A,B,C,D,i,j):
    if i>4 and j>5:
        return ric
    else:
        for x in range(A+i,A+j):
            for y in range(C,D+1):
                if x<y:
                    print(x,y)
        return ric(A,B,C,D,i+1,j+1)

main()