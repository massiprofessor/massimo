import random as r
import time
password= input("Inserire password: ")

#Dato che i requisiti della password sono: 1 maiusc, 1 min, 1 numero,
#1 carattere spec, 8 caratteri
#impostiamo le variabili che contengono al momento lo stato false a indicare
#che all'inizio del programma non abbiamo trovato i requisti
is_maiusc=False
is_minimo=False
is_num=False
is_check_spec=False
is_check_final=False

#Nel caso in cui la password non rispetta i requisiti definiamo delle variabili
#che contengono l'alfabeto utile per generare una nuova password
numeri="0123456789"
alfabeto_maiusc="ABCDEFGHIL"
alfabeto_min="abcdefghil"
spec="!#@$&=%-_*"

passw_gen=""

#Controllo requisiti password immessa dall'utente 
for elem in password:
    if elem.isupper() == True:
        is_maiusc=True # maiuscolo
    elif elem.islower() == True:
        is_minimo = True #minuscolo
    elif elem.isdigit() == True:
        is_num= True # è un numero
    elif elem in spec:
        is_check_spec=True # è un carattere speciale

#Se tutte le variabili di controllo sono vere allora rispetta i requisiti
if is_maiusc == True and is_minimo == True and is_num ==True and is_check_spec==True:
        is_check_final=True

        
#Se rispetta i requisiti e la password è lunga almeno 8 caratteri
#la password è sicura
if len(password) >= 8 and is_check_final == True:
    print("La password scelta è sicura")
else:
    #se la password non è sicura
    print("La password che hai scritto è insicura....ti sto generando una nuova password")
    for i in range(50):
        print(".",end="")
        time.sleep(0.05)
    #Parte il processo per generare una nuova password
    #Il ragionamento si basa sul seguente schema
    #Alfabeto delle lettere, numeri e caratteri speciali abbiamo deciso che siano 10
    #Vogliamo scegliere 3 lettere masiuscole
    #Vogliamo scelgliere 3 lettere minuscole
    #Voglioamo scegliere 1 numero
    #Vogliamo scelgliere 1 carattere speciale
    #Esempio AAAaaa1!
    for i in range(6):
        n_casual= r.randint(0,9)
        if i <= 2:
            passw_gen=passw_gen + alfabeto_maiusc[n_casual]
        else:
            passw_gen=passw_gen + alfabeto_min[n_casual]
    n_casual= r.randint(0,9)
    passw_gen= passw_gen + numeri[n_casual]
    passw_gen= passw_gen + spec[n_casual]
    print("\nLa passwod che ti consiglio è questa:",passw_gen)
            
    
    
