n=input()
trovato=True
while n!=".":
    if not n.isalpha():
        trovato=False
    n=input()

if trovato:
    print("SI",end="")
else:
    print("NO",end="")