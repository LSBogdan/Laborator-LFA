f = open("Date.txt")
Sigma = set()
States = set()
Transitions = []
StrInit = ''
StrFin = []
lista = []
cuv = []
ok = 0
nrF = 0

for linie in f:
    ok += 1
    if ok == 1:
       lista = []
       lista = linie.split(" ")
       n = int(lista[0])
       m = int(lista[1])
      
    elif ok < m + 2:
        linie = linie.replace("\n","")
        linie = linie.replace("\t","")
        linie = linie.strip() 
        lista = []
        lista = linie.split()
        States.add(lista[0])
        States.add(lista[1])
        Sigma.add(lista[2])
        Transitions.append(lista)

    elif ok == m + 2:
        linie = linie.replace("\n","")
        linie = linie.replace("\t","")
        linie = linie.replace(" ", "")
        linie = linie.strip()
        StrInit = linie
    
    elif ok == m + 3:
        StrFin = linie.split()
        nrF = int(StrFin[0])
        del StrFin[0]

        
    elif ok == m + 4:
        nrstringuri = int(linie)
    
    else:
        linie = linie.replace("\n","")
        linie = linie.replace("\t","")
        linie = linie.replace(" ", "")
        cuv.append(linie)


for word in cuv: 

    StrCrt = StrInit
    lungime = 0    
    lista = []
    ok = 0

    for i in word: 
        lungime+=1
        for j in Transitions: 
            ok1 = 0
            if i == j[2] and StrCrt == j[0]:
                StrCrt = j[1]
                lista.append(j[0])
                ok1 = 1

            if StrCrt in StrFin and lungime == len(word):
                lista.append(StrCrt)
                ok = 1
                break

            if ok1:
                break

        if ok:
            print("DA")
            print("Traseu:",*lista)
            break
    
    if ok == 0:
        print("NU")

        
