N=input()
bool=False
while N!="*":
    if N=="0" or N=="1" or N=="2" or N=="3" or N=="4" or N=="5" or N=="6" or N=="7" or N=="8" or N=="9":
        bool=True
    N=input()
if bool==False:
    print("NESSUNA",end="")
else:
    print("ALMENO UNA",end="")