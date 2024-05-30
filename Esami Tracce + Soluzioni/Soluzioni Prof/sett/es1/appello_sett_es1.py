n=int(input())   

convert=[["M"],
        ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
        ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
        ["I","II","III","IV","V","VI","VII","VIII","IX"]]

cifre=[]
#con questa "funzione" si invertono i numeri ES. 1674-->4761
while n>0:              #finchè n maggiore di 0, perchè al minimo abbiamo 1,
    cifre.append(n%10)  #divido n per 10 e prendo il resto della divisione e la mettiamo in cifre
    n=n//10             #aggiornare il valore di n dividendo per 10 che ci restituisce il risultato intero della divisione
  
s=""                              
for i in range(len(cifre)-1,-1,-1): #(start,stop, incr) partiamo dall'ultima posizione della lista e ci spostiamo verso la prima, decrementando di 1
    s+=convert[3-i][cifre[i]-1]   #concatenare, 
                                  #(riga)=3(lunghezza massima)-i(a seconda di dove si trova il corrisponde ad uni,dec,migl,cen)
                                  #(colonna)=il valore che trovo in cifre di i, decrementato di 1 per far si che parta da 1 fino a 9 anzichè da 0 a 8
#i
#0 --> 3
#1 --> 2
#2 --> 1
#3 --> 0

print(s,end="") #stampare senza andare a capo alla fine