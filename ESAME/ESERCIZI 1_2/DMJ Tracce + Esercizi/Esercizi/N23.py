n=input()
vocali=("a","e","i","o","u")
trovato=False
while n!="*":
    if n in vocali:
        trovato=True
    n=input()
    
if trovato:
    print("ALMENO 1 VOCALE",end="")
else:
    print("NESSUNA VOCALE",end="")