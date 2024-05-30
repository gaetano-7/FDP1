from random import randint
def main():
    N=8
    grig=[[' ', 'O', 'O', ' ', 'O', 'O', ' ', 'O'],
          ['O', 'X', ' ', ' ', ' ', ' ', 'O', 'X'],
          ['X', 'X', 'X', ' ', 'O', 'X', ' ', 'X'],
          ['X', ' ', 'X', 'X', 'X', ' ', 'X', 'O'],
          [' ', 'X', 'X', ' ', ' ', 'O', ' ', ' '],
          [' ', 'O', ' ', ' ', ' ', 'O', 'X', ' '],
          ['O', 'X', 'X', 'O', 'O', 'X', ' ', 'O'],
          ['X', 'X', ' ', 'X', 'X', ' ', 'X', ' ']]
    #crea_griglia(N)
    printa(grig,N)
    gioco(grig,N)

# def crea_griglia(N):
#     m=[]
#     for i in range(N):
#         m.append([])
#         for j in range(N):
#             c=randint(0,2)
#             if c==0:
#                 m[i].append("O")
#             elif c==1:
#                 m[i].append("X")
#             elif c==2:
#                 m[i].append(" ")
#     return m

def printa(grig,N):
    for i in range(N):
        print(grig[i])

def controllo(N,grig):
    k=[]
    for i in range(N):
        for j in range(N):
            k.append(grig[i][j])
    f=0
    if " " not in k:
        f=1
    return f

def gioco(grig,N):
    while controllo(N,grig)!=1:
        car=str(input())
        i=int(input())
        j=int(input())
        if car=="X":
            grig[i][j]="X"
            #ORIZZONTALE
            l=[]
            for k in range(N):
                l.append(grig[i][k])
            for h in range(len(l)-3):
                c=l[h]+l[h+1]+l[h+2]+l[h+3]
                if c=="XXXX":
                    grig[i][j]=" "
            #VERTICALE
            w=[]
            for s in range(N):
                w.append(grig[s][j])
            for r in range(len(w)-3):
                f=w[r]+w[r+1]+w[r+2]+w[r+3]
                if f=="XXXX":
                    grig[i][j]=" "
            #DIAGONALE
            diag=[]
            for q in range (len(grig[0])+N - 1):
                diag.append([])
            for a in range(len(grig[0])):
                for v in range(N):
                    diag[a-v-(-N+1)].append(grig[a][v])
            d=[]
            for p in range(len(diag)):
                if len(diag[p])>=4:
                    d.append(diag[p])
            
            for bi in range(len(d)):
                for bj in range(len(d[bi])-3):
                    lix=d[bi][bj]+d[bi][bj+1]+d[bi][bj+2]+d[bi][bj+3]
                    if lix=="XXXX":
                        grig[i][j]=" "

            diag2=[]
            for qq in range(N+len(diag)-1):
                diag2.append([])
            for aa in range(len(grig[0])):
                for vv in range(N):
                    diag2[aa+vv].append(grig[vv][aa])
            dd=[]
            for pp in range(len(diag2)):
                if len(diag2[pp])>=4:
                    dd.append(diag2[pp])
            
            for bii in range(len(dd)):
                for bjj in range(len(dd[bii])-3):
                    lixx=dd[bii][bjj]+dd[bii][bjj+1]+dd[bii][bjj+2]+dd[bii][bjj+3]
                    if lixx=="XXXX":
                        grig[i][j]=" "

            printa(grig,N)
        
        if car=="O":
            grig[i][j]="O"
            #ORIZZONTALE
            l=[]
            for k in range(N):
                l.append(grig[i][k])
            for h in range(len(l)-3):
                c=l[h]+l[h+1]+l[h+2]+l[h+3]
                if c=="OOOO":
                    grig[i][j]=" "
            #VERTICALE
            w=[]
            for s in range(N):
                w.append(grig[s][j])
            for r in range(len(w)-3):
                f=w[r]+w[r+1]+w[r+2]+w[r+3]
                if f=="OOOO":
                    grig[i][j]=" "
            #DIAGONALE
            diag=[]
            for q in range (len(grig[0])+N - 1):
                diag.append([])
            for a in range(len(grig[0])):
                for v in range(N):
                    diag[a-v-(-N+1)].append(grig[a][v])
            d=[]
            for p in range(len(diag)):
                if len(diag[p])>=4:
                    d.append(diag[p])
            
            for bi in range(len(d)):
                for bj in range(len(d[bi])-3):
                    lix=d[bi][bj]+d[bi][bj+1]+d[bi][bj+2]+d[bi][bj+3]
                    if lix=="OOOO":
                        grig[i][j]=" "

            diag2=[]
            for qq in range(N+len(diag)-1):
                diag2.append([])
            for aa in range(len(grig[0])):
                for vv in range(N):
                    diag2[aa+vv].append(grig[vv][aa])
            dd=[]
            for pp in range(len(diag2)):
                if len(diag2[pp])>=4:
                    dd.append(diag2[pp])
            
            for bii in range(len(dd)):
                for bjj in range(len(dd[bii])-3):
                    lixx=dd[bii][bjj]+dd[bii][bjj+1]+dd[bii][bjj+2]+dd[bii][bjj+3]
                    if lixx=="OOOO":
                        grig[i][j]=" "
            printa(grig,N)

main()