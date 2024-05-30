l=[]
for i in range(10):
    l.append(int(input()))
x=int(input())

lix=True

for i in l:
    if i%x==0:
        lix=False      
        
if lix:
    print("OK",end="")
else:
    print("NO",end="")
    