vocale_last = False
vocali = ["a","e","i","o","u"]
sequenze = 1

lettera = input()
vocale_last = bool(lettera in vocali)
if(lettera == "."):
    sequenze = 0
else:
    while True:
        lettera = input()

        if(lettera == "."):
            break

        if((lettera in vocali)==vocale_last):
            sequenze += 1
        

        vocale_last = bool(lettera in vocali)

    
print(sequenze, end="")