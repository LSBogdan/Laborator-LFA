import argparse


def get_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help="dfa_config_file")
    parser.add_argument('word', help="word_input")
    args = parser.parse_args()

    return args.file, args.word


Exemplu, word = get_line_arguments()

f = open(Exemplu, "r")
Sigma = set()
States = set()
Transitions = []
StrInit = ''
StrFin = []
lista = []
ok = ok1 = 0
nrS = nrF = 0

for linie in f:
    if linie[0] != "#":
        if "Sigma" in linie or "States" in linie or "Transitions" in linie or "End" in linie:
            ok += 1
            continue

        else:
            if ok == 1:
                linie = linie.replace("\n", "")
                linie = linie.replace("\t", "")
                linie = linie.strip()
                Sigma.add(linie)

            elif ok == 3:
                linie = linie.replace("\n", "")
                linie = linie.replace("\t", "")
                linie = linie.strip()
                if 'S' in linie:
                    nrS += 1
                    States.add(linie[:linie.find(",")])
                    StrInit = linie[:linie.find(",")]
                    if nrS > 1 and ok1 == 0:
                        print("Eroare, avem mai mult de o stare initiala!")
                        ok1 = 1

                elif 'F' in linie:
                    nrF += 1
                    States.add(linie[:linie.find(",")])
                    StrFin.append(linie[:linie.find(",")])
                else:
                    States.add(linie)

            else:
                linie = linie.replace("\n", "")
                linie = linie.replace("\t", "")
                linie = linie.replace(" ", "")
                linie = linie.strip()
                lista = []
                lista = linie.split(',')

                if lista[0] not in States:
                    print("Eroare, nu exista starea:", lista[0])

                if lista[1] not in Sigma:
                    print("Eroare, nu exista cuvantul:", lista[1])

                if lista[2] not in States:
                    print("Eroare, nu exista starea:", lista[2])

                if lista[0] in States and lista[1] in Sigma and lista[2] in States:
                    Transitions.append(lista)

if nrF == 0:
    print("Eroare, nu exista starea finala!")

if nrS == 1 and nrF:
    StrCrt = StrInit
    lungime = 0
    ok = 0
    for i in word:
        lungime += 1
        for j in Transitions:
            if i == j[1] and StrCrt == j[0]:
                StrCrt = j[2]

                if StrCrt in StrFin and lungime == len(word):
                    ok = 1
                    break
        if ok:
            print(">>accept")
            break
    if ok == 0:
        print(">>reject")


