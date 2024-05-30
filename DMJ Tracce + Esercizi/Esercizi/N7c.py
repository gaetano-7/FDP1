primo=0
secondo=0
terzo=0
i=0
n=int(input())
if n==1:
    primo+=1
elif n==2:
    secondo+=1
elif n==3:
    terzo+=1

while n!=0:
    n=int(input())
    i+=1
    if n==1:
        primo+=1
    elif n==2:
        secondo+=1
    elif n==3:
        terzo+=1
    
if i!=0:
    roununo=round(primo/i*100,1)
    roundue=round(secondo/i*100,1)
    rountre=round(terzo/i*100,1)
    print(1,primo,roununo)
    print(2,secondo,roundue)
    print(3,terzo,rountre)

if roununo>50:
    print("VINCE 1",end="")
elif roundue>50:
    print("VINCE 2",end="")
elif rountre>50:
    print("VINCE 3",end="")
else:
    print("BALLOTTAGGIO",end="")


    