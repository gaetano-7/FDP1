anno=int(input())

if anno%400 == 0:
    print("BISESTILE", end="")
elif anno%100 != 0 and anno%4 == 0:
    print("BISESTILE", end="")
else:
    print("NON BISESTILE", end="")