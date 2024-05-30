A=[]
for i in range(26):
    s=str(input())
    A.append(s)
N=int(input())
B=[]
for i in range (N):
    B.append(int(input()))
    
parola=[]
for i in range(len(B)):
    if B[i]<26:
        parola.append(A[B[i]])

for i in parola:
    print(i,end="")