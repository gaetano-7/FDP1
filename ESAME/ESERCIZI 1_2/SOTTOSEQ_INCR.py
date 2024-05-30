def main():
    seq=leggi_seq()
    d=gioco(seq)
    print(d,end="")


def leggi_seq():
    s=[]
    n=input()
    while n!="*":
        s.append(int(n))
        n=input()
    return s

def gioco(seq):
    s=[]
    for i in range(len(seq)-1):
        if seq[i]==seq[i+1]-1:
            s.append(seq[i])
        else:
            s.append("_")
        
    s.insert(0,"_")
    s.append("_")
    co=0
    for i in range(len(s)-1):
        if s[i]=="_" and s[i+1]!="_":
            co+=1
    return co

        
            

main()