def bin_dec_vic(d,is_dec):
    if is_dec == True:
        b=""
        while d>0:
            b= b + str(d%2) #101
            d= d//2
        return b[::-1]
    else:
        pot=len(d)-1
        dec=0
        for elem in d:
            if elem == "1":
                dec= dec + 2**pot
            pot= pot -1
        return dec
            







while True:
    scelta=input("1.per convertire in binario\n2. per convertire in decimale\n3. Uscire\n\n")
    if scelta=="1":
        try:
            dec=int(input("Inserisci decimale da convertire in bin: "))
            is_dec=True
            binario=bin_dec_vic(dec,is_dec)
            print(dec,"---->",binario)
        except ValueError:
            print("Hai inserito un tipo di dato non corretto")
    elif scelta =="2":
        binario=input("Inserisci binario da convertire in dec: ")
        is_dec=False
        decimale=bin_dec_vic(binario,is_dec)
        print(binario,"----->",decimale)
    elif scelta=="3":
        print("Arrivederci e grazie")
        break
                
    

    
