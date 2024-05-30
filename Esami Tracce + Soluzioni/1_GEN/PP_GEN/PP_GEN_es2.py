n_est=[]
n_gio=[]

for i in range(10):
    n_est.append(int(input()))
for i in range(10):
    n_gio.append(int(input()))

cont=0
cont_max=0

for i in range(10):
    while (i+cont<len(n_gio)  and  n_gio[i+cont] in n_est):
        cont+=1
    if (cont>cont_max):
        cont_max=cont
    cont=0
    
if (cont_max>1 and cont_max<=5):
    print(cont_max,end="")
else:
    print(0,end="")
    