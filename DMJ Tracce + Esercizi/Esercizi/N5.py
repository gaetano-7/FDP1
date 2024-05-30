a=int(input())
b=int(input())
c=int(input())

if a < b+c and b < a+c and c < a+b:
    if a == b and b == c:
        print("TRIANGOLO EQUILATERO", end="")
    elif a != b and b != c:
        print("TRIANGOLO SCALENO", end="")
    else:
        print("TRIANGOLO ISOSCELE", end="")
else:
    print("NO", end="")