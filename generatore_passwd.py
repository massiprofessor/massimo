import random as r
numeri="0123456789"
alfabeto_maiusc="ABCDEFGHIL"
alfabeto_min="abcdefghil"
caratteri_spec="!#@$&=%-_*"

passw_gen=""
for i in range(6):
    n_casual= r.randint(0,9)
    if i <= 2:
        passw_gen=passw_gen + alfabeto_maiusc[n_casual]
    else:
        passw_gen=passw_gen + alfabeto_min[n_casual]

n_casual= r.randint(0,9)
passw_gen= passw_gen + numeri[n_casual]
passw_gen= passw_gen + caratteri_spec[n_casual]

print(passw_gen)
    
