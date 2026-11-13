# exercie n° 1 python
from cheroot.workers.threadpool import trueyzero


def nomprenom():
    nom = str(input("nom :"))
    prenom = str(input("prenom :"))
    nom = str.upper(nom)
    prenom = str.capitalize(prenom)
    print(f"""
        {nom}
        {prenom}
    """)
# nomprenom()

# exo n° 2 python
def fonction():
    sum = 0
    nb = 0
    test_8 = False
    for i in range(5):
        inp = str(input("Veuillez entrer la note du module 1 et le coefficient correspondant :"))
        ltemp = inp.split(" ")
        val = float(ltemp[0])
        coef = float(ltemp[1])
        nb+= coef
        sum += val * coef
        if val < 8:
            test_8 = True
    print(sum/nb)
    if sum/nb >= 10 and test_8 == False:
        print("Admis")
    else:
        print("Refusé")
# fonction()

from math import floor
def validatestr():
    inp = str(input("Entrez un mot ou une phrase :"))
    phrase = ""
    test = False
    for i in inp:
        if i.isalpha():
            phrase += i
    phrase = phrase.lower()
    for i in range(floor(len(phrase)/2)):
        if phrase[i] != phrase[-(i+1)]:
            test = True
    if test == False:
        print("Palindrome")
    else:
        print("Pas Palindrome")
# validatestr()

def exo4():
    sum = int(input())
    dico= {"100":0, "50":0, "10":0, "2":0, "1":0}
    while sum > 0:
        if (sum - 100) > 0:
            dico["100"] += 1
            sum -= 100
        elif (sum - 50) >0:
            dico["50"] += 1
            sum -= 50
        elif (sum - 10) >0:
            dico["10"] += 1
            sum -= 10
        elif (sum - 2) >0:
            dico["2"] += 1
            sum -= 2
        else:
            dico["1"] += 1
            sum -= 1
    print(dico)
# exo4()

def exo5():
    nbh = int(input("nb heures:"))
    sh = float(input("salaire horraire:"))
    q1 = 160
    q2 = 200
    salaire = 0
    for i in range(nbh):
        if i < q1:
            salaire +=  sh
        elif i < q2:
            salaire += 1.25 * sh
        else:
            salaire += 1.5 * sh
    print(salaire)
#
# exo5()
def exo6():
    txt = str(input("txt:"))
    count = 0
    for i in txt:
        count+=1
    count_v = 0
    mot = 0
    txt = txt.lower()
    for i in txt:
        if i in ["a","i","u","e","o"]:
            count_v += 1


    print(count_v)
    print(count)
# exo6()

import os.path as p
def exo7():
    path = str(input())
    if p.isfile(path):
        return (True)
    else:
        return