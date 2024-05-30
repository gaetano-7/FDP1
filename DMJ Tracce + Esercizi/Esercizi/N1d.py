SaldoCorr=500
CanoneM=5
Inte=2*SaldoCorr/100
X=SaldoCorr
Y=((SaldoCorr-5)+(Inte))
Z=((Y-5)+Inte)

print("PRIMO MESE:",X)
print("PRIMO MESE:",round(Y))
print("PRIMO MESE:",round(Z),end="")


