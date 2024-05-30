s_corr=int(input())
c_mens=int(input())
perc=int(input())

inte=perc*s_corr/100
secondo=((s_corr-c_mens)+inte)
terzo=((secondo-c_mens)+inte)

print("PRIMO MESE:",s_corr)
print("PRIMO MESE:",round(secondo))
print("PRIMO MESE:",round(terzo),end="")