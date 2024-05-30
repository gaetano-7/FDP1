c_mat=int(input()) 
ore_lavo=int(input()) 
min=100
costo=40

totale=ore_lavo*costo+c_mat

if totale<min:
    print(min,end="")
else:
    print(totale,end="")



