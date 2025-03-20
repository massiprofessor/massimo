import sys
sys.path.append('C:\\Users\\Cisco\\Desktop') # se il modulo è in una cartella diversa da quella dello script principale
from modulos import somma as s

n1= int(input("Inserisci numero: "))
n2= int(input("Inserisci numero: "))
x=s(n1,n2)
print(x)
