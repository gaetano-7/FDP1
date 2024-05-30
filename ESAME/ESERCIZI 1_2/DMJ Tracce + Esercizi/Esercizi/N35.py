tappo=1
tempo=0
while tappo!=0:
    x=int(input())
    if  x != 0:
        y = str(input())
        if y == "s":
            tempo += x
        elif y == "m":
            tempo += (x*60)
        elif y == "h":
            tempo += (x*60*60)
        else:
            break
    else:
        tappo = 0
print(tempo, end="")
