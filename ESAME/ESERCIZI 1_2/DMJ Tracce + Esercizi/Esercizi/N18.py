n=input()

a="abc"
count=0

while True:
    
    if (n!="o" and n!="k"):
        count+=1
    elif (n=="k" and a!="o"):
        count+=1
        
    if (a=="o"):
        if(n=="k"):
            break
        count+=1
        
    a=n
    n=input()
    
print(count,end="")