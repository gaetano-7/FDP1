N = input()
C = False
while N != '*':
    M = N 
    N = input()
    if  (N.isalpha() and M.isalpha()) and ((N.islower() and M.islower() and N==M) or (N.isupper() and M.isupper())):
        C = True
if C:
    print('SI', end='')
else:
    print('NO', end='')