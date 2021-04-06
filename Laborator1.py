f = open("LFA - L1 - Exemplu 1.txt") 

Sigma = set()
States = set()
lista = []
ok = 0
nrS = nrF = 0
ok1 = 0
for linie in f:
    if linie[0]!= "#":
        if "Sigma" in linie  or "States" in linie or "Transitions" in linie or "End" in linie:
            ok+=1
            continue

        else:
            if  ok == 1:
                linie = linie.replace("\n","")
                linie = linie.replace("\t","")
                linie = linie.strip()
                Sigma.add(linie)

            elif ok == 3:
                linie = linie.replace("\n","")
                linie = linie.replace("\t","")
                linie = linie.strip() 
                if 'S' in linie:
                    nrS+=1
                    States.add(linie[:linie.find(",")])
                    if nrS > 1 and ok1 ==0 :
                         print("Eroare, avem mai mult de o stare initiala")
                         ok1 = 1

                elif 'F' in linie:
                    nrF+=1
                    States.add(linie[:linie.find(",")])
                else:
                    States.add(linie)

            else:
                linie = linie.replace("\n","")
                linie = linie.replace("\t","")
                linie = linie.replace(" ", "")
                linie = linie.strip() 
                lista = []
                lista = linie.split(',')
            
                if lista[1] not in Sigma:
                    print("Eroare, nu exista cuvantul:",lista[1])
                if lista[0] not in States:
                    print("Eroare, nu exista starea:",lista[0])
                if lista[2] not in States:
                    print("Eroare, nu exista starea:",lista[2])
                
