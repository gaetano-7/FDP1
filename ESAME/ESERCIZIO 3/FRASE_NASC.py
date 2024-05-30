def main():
    N=7
    M=5
    mat=[['1','L','U','N','A'],
         ['D','I','1','U','N'],
         ['1','B','E','T','A'],
         ['A','R','T','E','1'],
         ['D','O','1','L','1'],
         ['E','1','G','L','I'],
         ['1','G','R','A','N']]
    seq=[2,5,2,4]
    st='01o.gs*13o11vcasa01v15oooo10oxs:130osalto'
    s=sequenze(st,N,M)
    r_mat=revers(mat,N,M)
    yu=gioco(s,seq,mat,r_mat,N,M)
    print(yu,end="")

def sequenze(st,N,M):
    num_i=[]
    num_j=[]
    for i in range(N):
        num_i.append(str(i))
    for j in range(M):
        num_j.append(str(j))
    l=[]
    for i in range(len(st)-2):
        d=[]
        if st[i] in num_i and st[i+1] in num_j and st[i+2]=="o" or st[i+2]=="v":
            d.append(st[i])
            d.append(st[i+1])
            d.append(st[i+2])
        if len(d)==3:
            l.append(d)
    return l

def revers(mat,N,M):
    r=[]
    for i in range(M):
        r.append([])
        for j in range(N):
            r[i].append(mat[j][i])
    return r

def gioco(s,seq,mat,r_mat,N,M):
    f=0
    tutto=[]
    for i in range(len(s)):
        if s[i][2]=="o":
            paro=[]
            if '1' in mat[int(s[i][0])]:
                uno=mat[int(s[i][0])].index('1')
            if uno<int(s[i][1]):
                paro=mat[int(s[i][0])][int(s[i][1]):]
            else:
                paro=mat[int(s[i][0])][int(s[i][1]):uno]
            if len(paro)==seq[f]:
                tutto.append(paro)
                f+=1

        if s[i][2]=="v":
            paro=[]
            if '1' in r_mat[int(s[i][1])]:
                uno=r_mat[int(s[i][1])].index('1')
            if uno<int(s[i][0]):
                paro=r_mat[int(s[i][1])][int(s[i][0]):]
            else:
                paro=r_mat[int(s[i][1])][int(s[i][0]):uno]
            if len(paro)==seq[f]:
                tutto.append(paro)
                f+=1
    gre=""
    for i in range(len(tutto)):
        for j in range(len(tutto[i])):
            gre=gre+tutto[i][j]
        gre=gre+" "
    return gre



main()