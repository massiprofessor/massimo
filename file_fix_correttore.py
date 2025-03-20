try:
    f= open(r"C:\Users\Cisco\Desktop\massimo.txt","r")
    contenuto=f.read()
    f.close()
    #Speriamo che esce il soleNon è colpa di fabio
    contenuto= contenuto.split(" ")
    #["Speriamo", "che", "esce", "il", "soleNon", "è", "colpa", "di", "fabio"]
    contenuto_fix=""
    for elem in contenuto:
        if "sole" not in elem:
            contenuto_fix= contenuto_fix + " " + elem
        else:
            contelem=""
            for e in elem:
                if e != "e":
                    contelem=contelem + e
                else:
                    contelem= contelem + e + " "
            contenuto_fix= contenuto_fix + " " + contelem

    f= open(r"C:\Users\Cisco\Desktop\massimo.txt","w")
    f.write(contenuto_fix)
    f.close()
except FileNotFoundError:
    print("Il file non esiste")

    
    
