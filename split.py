ip="192.168.1.146"
#ip=["192","168","1","146"]
ip= ip.split(".")
print(ip)

print()


email="massimo@libero.it"
username= email.split("@")
print(username[0])

print()


utente="root:1:150:'gtfgfgdfgds435423!'"
utente=utente.split(":")
username=utente[0]
id_utente= utente[1]
group_utente=utente[2]
passw=utente[3]
print("Username",username)
print("ID",id_utente)
print("Gruppo-ID",group_utente)
print("Password",passw)
