#Errore personalizzato
class MassimoCasual(Exception):
    pass #serve a non lasciare vuoto un blocco di programmazione che potrà essere scritto in seguito

raise MassimoCasual("Oggi massimo non si è vestito bene per il feedback")




try:
    raise ZeroDivisionError ("Questo è dato non può essere zero")
    raise ValueError ("Questo è un dato non corretto")
except:
    print("Ciao")
    raise   #rilasciare l'errore nell'ordine del try
