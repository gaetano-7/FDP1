consec=False
last=""
while True:
    n=input()
    if n=="*":
        break
    if n==last:
        consec=True
        
    last=n
    
if consec:
    print("SI",end="")
else:
    print("NO",end="")