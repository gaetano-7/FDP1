N=int(input())
s=str(N)
L=[]
for i in range(len(s)):
    L.append(int(s[i]))
    
rom=[]
if len(L)==4:
    if L[0]==1:
        rom.append("M")
    if L[1]!=0:
        if L[1]==1:
            rom.append("C")
        elif L[1]==2:
            rom.append("CC")
        elif L[1]==3:
            rom.append("CCC")
        elif L[1]==4:
            rom.append("CD")
        elif L[1]==5:
            rom.append("D")
        elif L[1]==6:
            rom.append("DC")
        elif L[1]==7:
            rom.append("DCC")
        elif L[1]==8:
            rom.append("DCCC")
        elif L[1]==9:
            rom.append("CM")
    if L[2]!=0:
        if L[2]==1:
            rom.append("X")
        elif L[2]==2:
            rom.append("XX")
        elif L[2]==3:
            rom.append("XXX")
        elif L[2]==4:
            rom.append("XL")
        elif L[2]==5:
            rom.append("L")
        elif L[2]==6:
            rom.append("LX")
        elif L[2]==7:
            rom.append("LXX")
        elif L[2]==8:
            rom.append("LXXX")
        elif L[2]==9:
            rom.append("XC")
    if L[3]!=0:
        if L[3]==1:
            rom.append("I")
        elif L[3]==2:
            rom.append("II")
        elif L[3]==3:
            rom.append("III")
        elif L[3]==4:
            rom.append("IV")
        elif L[3]==5:
            rom.append("V")
        elif L[3]==6:
            rom.append("VI")
        elif L[3]==7:
            rom.append("VII")
        elif L[3]==8:
            rom.append("VIII")
        elif L[3]==9:
            rom.append("IX")
elif len(L)==3:
    if L[0]==1:
        rom.append("C")
    elif L[0]==2:
        rom.append("CC")
    elif L[0]==3:
        rom.append("CCC")
    elif L[0]==4:
        rom.append("CD")
    elif L[0]==5:
        rom.append("D")
    elif L[0]==6:
        rom.append("DC")
    elif L[0]==7:
        rom.append("DCC")
    elif L[0]==8:
        rom.append("DCCC")
    elif L[0]==9:
        rom.append("CM")
    if L[1]!=0:
        if L[1]==1:
            rom.append("X")
        elif L[1]==2:
            rom.append("XX")
        elif L[1]==3:
            rom.append("XXX")
        elif L[1]==4:
            rom.append("XL")
        elif L[1]==5:
            rom.append("L")
        elif L[1]==6:
            rom.append("LX")
        elif L[1]==7:
            rom.append("LXX")
        elif L[1]==8:
            rom.append("LXXX")
        elif L[1]==9:
            rom.append("XC")
    if L[2]!=0:
        if L[2]==1:
            rom.append("I")
        elif L[2]==2:
            rom.append("II")
        elif L[2]==3:
            rom.append("III")
        elif L[2]==4:
            rom.append("IV")
        elif L[2]==5:
            rom.append("V")
        elif L[2]==6:
            rom.append("VI")
        elif L[2]==7:
            rom.append("VII")
        elif L[2]==8:
            rom.append("VIII")
        elif L[2]==9:
            rom.append("IX")
elif len(L)==2:
    if L[0]==1:
        rom.append("X")
    elif L[0]==2:
        rom.append("XX")
    elif L[0]==3:
        rom.append("XXX")
    elif L[0]==4:
        rom.append("XL")
    elif L[0]==5:
        rom.append("L")
    elif L[0]==6:
        rom.append("LX")
    elif L[0]==7:
        rom.append("LXX")
    elif L[0]==8:
        rom.append("LXXX")
    elif L[0]==9:
        rom.append("XC")
    if L[1]!=0:
        if L[1]==1:
            rom.append("I")
        elif L[1]==2:
            rom.append("II")
        elif L[1]==3:
            rom.append("III")
        elif L[1]==4:
            rom.append("IV")
        elif L[1]==5:
            rom.append("V")
        elif L[1]==6:
            rom.append("VI")
        elif L[1]==7:
            rom.append("VII")
        elif L[1]==8:
            rom.append("VIII")
        elif L[1]==9:
            rom.append("IX")
elif len(L)==1:
    if L[0]==1:
        rom.append("I")
    elif L[0]==2:
        rom.append("II")
    elif L[0]==3:
        rom.append("III")
    elif L[0]==4:
        rom.append("IV")
    elif L[0]==5:
        rom.append("V")
    elif L[0]==6:
        rom.append("VI")
    elif L[0]==7:
        rom.append("VII")
    elif L[0]==8:
        rom.append("VIII")
    elif L[0]==9:
        rom.append("IX")

num=""           
for i in range(len(rom)):
    num+=str(rom[i])
    
print(num,end="")