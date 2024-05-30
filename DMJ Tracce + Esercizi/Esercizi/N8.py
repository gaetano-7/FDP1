x=int(input())
y=int(input())
somma=0
while (x<=y):
    if x%2==1:
        somma=x+somma
    x=x+1
print(somma,end="")