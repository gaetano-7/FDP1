numero = input() #prendi il primo numero da input
lista = [] # crea una lista vuota
while numero != "*": # ciclo while finchè il numero è diverso da "*"
    lista.append(int(numero)) # aggiunge i numeri presi da input alla lista
    numero = input() # prendi numeri da input

contatore = 0 # contatore inizializzato a 0 per conservare il numero di incrementi max
lunghezza = 0   # variabile inizializzata a 0

for i in range(0, len(lista)-1): # ciclo for che va da 0 alla lunghezza della lista -1 perchè l'ultimo non serve in quanto non ha un successivo
    if lista[i+1] == lista[i]+1: # condizione  if se l'elemento successivo ad i(seq[i+1]) è uguale all'elemento i-esimo +1
        if i == len(lista)-2: # condizione if se sono nell'ultima posizione per il controllo e il successivo è incrementale
            contatore += 1   # incrementa il contatore, altrimenti il contatore rimane a 1
        lunghezza += 1   # quando mi trovo in una seq incrementale, incremento lunghezza
    else:  #invece quando due elementi non sono più incrementali
        if lunghezza > 0: #se la variabile lunghezza > 0 vuol dire che prima l'avrò incrementato, quindi la seq incr è finita
            contatore += 1  # incrementa il numero di seq incr
        lunghezza = 0 # inizializzo di nuovo uguale a 0
print(contatore,end="") # stampa il numero di sequenze incrementali trovate