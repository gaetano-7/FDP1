def main():
    C=['a','*','w']
    I=[1,13]
    lix(C,I,0)

def lix(char,inte,i):
    if i>1:
        return lix
    else:
        print(inte[i],char[0],char[1],sep="")
        print(inte[i],char[0],char[2],sep="")
        print(inte[i],char[1],char[0],sep="")
        print(inte[i],char[1],char[2],sep="")
        print(inte[i],char[2],char[0],sep="")
        print(inte[i],char[2],char[1],sep="")
    return lix(char,inte,i+1)

main()