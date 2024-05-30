def main():
    seq=leggi_seq()
    gioco(seq)

def leggi_seq():
    s=[]
    n=input()
    while n!=".":
        s.append(int(n))
        n=input()
    return s

def gioco(seq):
    d=""
    for i in range(len(seq)):
        if i%2!=0:
            for j in range(seq[i-1]):
                d+=str(seq[i])
    print(d)
main()