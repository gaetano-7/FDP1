com=0
listacom=[] 
while com!=9:   
    com=int(input())
    if (com>0 and com<8) and len(listacom)<100:
        listacom.append(com)
    elif com==9:
        break
    
print(listacom)