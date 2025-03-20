import ast


def check(nome):
    if nome in registro:
        is_check=True
    else:
        is_check=False
    return is_check

def insnomi(nome,is_check):
    is_check= check(nome)
    if is_check ==False:
        registro.update({nome:[]})
        scrivi()
    else:
        print("Il nome esiste già")

def insvoti(nome,is_check):
    is_check= check(nome)
    if is_check ==True:
        try:
            voto= int(input("Inserisci voto: "))
            registro[nome].append(voto)
            scrivi()
        except ValueError:
            print("Hai inserito un voto non corretto")
    else:
        print("Il nome non esiste nel registro")
    
    
def visualizza():
    if len(registro) == 0:
        print("Il registro è vuoto")
    else:
        print("Nome ---------- Voti")
        spazio=15
        for elem in registro:
            print(elem + " "*(spazio - len(elem)) + str(registro[elem]))

def scrivi():
    f= open(r"C:\Users\Cisco\Desktop\registro.txt","w")
    f.write(str(registro))
    f.close()


                 

try:
    f= open(r"C:\Users\Cisco\Desktop\registro.txt","r")
    contenuto=f.read()
    f.close()
    if len(contenuto) == 0:
        registro={}
    else:
        registro=ast.literal_eval(contenuto)
except FileNotFoundError:
    f= open(r"C:\Users\Cisco\Desktop\registro.txt","w")
    registro={}
    f.close()





while True:
    scelta=input("1. inserire nomi\n2. inserire voti\n3. visualizzare voti\n4. Uscire\n\n")
    if scelta=="1":
        nome=input("Inserisci nome: ")
        is_check= check(nome)
        insnomi(nome, is_check)
    if scelta=="2":
        nome=input("Inserisci nome: ")
        is_check= check(nome)
        insvoti(nome,is_check)
    if scelta=="3":
        visualizza()
    if scelta=="4":
        print("Ciao")
        break
        
            
        
