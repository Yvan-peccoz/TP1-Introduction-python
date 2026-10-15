#- ------------------- EXO N°1 :

def Table():
    nb = float(input("Vous cherchez la table de multiplication de quel nombre ?"))
    coeff = 0
    for i in range(10):
        res = round(coeff * nb, 1)
        print(f"{nb} * {coeff} = {res}")
        coeff += 1
    return res
#Table()


#- ------------------- EXO N°2 :

def Moy():
    nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
    moyenne = 0.0
    notes = []
    for i in range(nombreEtudiants):
        nt_etud = float(input(f"Note étudiant {i} : "))
        notes.append(nt_etud)
        moyenne += nt_etud
    moyenne /= nombreEtudiants
    print(f"Moyenne de classe : {moyenne}")
    print(f"Numéro de l’Etudiant | note | écart a la moyenne")
    for i in range(nombreEtudiants):
        print(f"{i} | {notes[i]} | {notes[i]-moyenne}")
#Moy()

#- ------------------- EXO N°2 :
def Scal(nMax=3):
    v1 = []
    v2 = []
    scal = 0
    n = int(input("Veuillez entrer la taille effective des vecteurs: "))
    while n < 1 or n > nMax:
        n = int(input("Veuillez entrer la taille effective des vecteurs: "))
    print("Saisie du premier vecteur : ")
    for i in range(n):
        v1.append(int(input(f"v1[{i}] = ")))
    print("\nSaisie du srcond vecteur : ")
    for i in range(n):
        v2.append(int(input(f"v2[{i}] = ")))
        scal += v1[i]*v2[i]
    print(f"\nLe produit scalaire de v1 par v2 vaut 39.0")

#Scal()

def exo4_1():
    lst = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]
    cmpf = 0
    valf = 0
    valt = lst[0]
    cmpt = 1
    for i in range(1,len(lst)):
        for j in range(i, len(lst)):
            if lst[j] == valt:
                cmpt += 1
        if cmpt > cmpf:
            cmpf = cmpt
            valf = valt
        valt = lst[i]
        cmpt = 1
    print(f"le nombre le plus fréquent est : {valf} ({cmpf} x)")
#exo4_2()
def exo4_2():
    lst = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]
    valf = lst[0]
    cmpf = 0
    for i in range(1,len(lst)):
        cmpt = lst.count(lst[i])
        if cmpt > cmpf:
            cmpf = cmpt
            valf = lst[i]
    print(f"le nombre le plus fréquent est : {valf} ({cmpf} x)")

#exo4_2()

def exo5():
    test = False
    lst = [2,9,0,2,2,0,2,2]
    m31 = [1,3,5,7,8,10,12]
    if len(lst)==8:
        j = str(lst[0]) + str(lst[1])
        m = str(lst[2]) + str(lst[3])
        an = str(lst[4]) + str(lst[5]) + str(lst[6]) + str(lst[7])
        j, m, an = int(j), int(m), int(an)
        if j >=1 and j<=31:
            if m >=1 and m<=12:
                if (m in m31) and (j==31):
                    test = True
                elif (m ==2) and (j<=29) and ((an%400 == 0) or (an%4 == 0) and (an%100 != 0)):
                    test = True
                elif m == 2 and j <= 28:
                    test = True
                elif j<31 and m!=2:
                    test = True
    return(test)

#print(exo5())

def exo6():
    lst = [5, 2, 4, 8, 1, 3]
    m = lst[0]
    id = 0
    for i in range(1,len(lst)):
        print(lst)
        for j in range(i+1,len(lst)):
            if lst[j]< m:
                m = lst[j]
                id = j
        lst[i], lst[id] = lst[id], lst[i]

exo6()