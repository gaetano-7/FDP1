def main():
    N=6
    D= [['ppp1', 'pippo', '20'], 
        ['plt5', 'pluto', '22'], 
        ['tpln3', 'topolino', '21'], 
        ['mnn2', 'minnie', '26'], 
        ['clrbll', 'clarabella','31'], 
        ['rzo1', 'orazio','28']]

    E= [['ppp1', 'NO'] , 
        ['tpln3', 'SI'], 
        ['mnn2', 'NO'], 
        ['plt5', 'SI'], 
        ['rzo1','SI'], 
        ['clrbll', 'SI']]

    M=2

    P= [['tpln5', 'topolina', '28'], 
        ['plt5', 'pluto', '22']]
    
    new_d(N,E,D,M,P)
    
    prima=[D[0][1],D[0][2],"anni","e",D[1][1],D[1][2],"anni"]
    seconda=[D[2][1],D[2][2],"anni","e",D[3][1],D[3][2],"anni"]

    pri=[int(D[0][2]),int(D[1][2])]
    sec=[int(D[2][2]),int(D[3][2])]
    
    tutt(D,pri,sec,seconda,prima)

def new_d(N,E,D,M,P):
    pop=[]
    for i in range(N):
        for j in range(N):
            if E[i][1]=='NO' and E[i][0]==D[j][0]:
                pop.append(D[j])
    for i in range(len(pop)):
        D.remove(pop[i])

    for i in range(M):
        if P[i] not in D:
            D.append(P[i])



def tutt(D,pri,sec,seconda,prima):
    if len(D)%2!=0:
        eta=[]
        pri_me=int(sum(pri)/len(pri))
        sec_me=int(sum(sec)/(len(sec)))
        ult=D[len(D)-1]
        if pri_me<int(D[len(D)-1][2]) and int(D[len(D)-1][2])<sec_me:
            seconda.append("e")
            for i in range(len(ult)):
                seconda.append(ult[1])
                seconda.append(ult[2])
                break
        for i in range(len(prima)):
            print(prima[i],end=' ')
        print()
        for i in range(len(seconda)):
            print(seconda[i],end=' ')
    else:
        for i in range(len(prima)):
            print(prima[i],end=' ')
        print()
        for i in range(len(seconda)):
            print(seconda[i],end=' ')

main()   