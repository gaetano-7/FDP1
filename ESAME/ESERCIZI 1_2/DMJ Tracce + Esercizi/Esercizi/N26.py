seq=""
n=input()
cons=0

while n!="*":      
    seq+=n
    n=input()

prec = ""
for i in seq:
    if prec.islower() and i.islower() and prec == i:
        cons += 1
        prec = i
    elif i.isupper() and prec.isupper():
        cons += 1
        prec = i
    else:
        prec = i
        

if cons > 0:
    print("SI", end="")
else:
    print("NO", end="")