#exo 1
def exo1(L1 = [0]*3):
    print(type(L1), id(L1))
    for i in L1:
        print(id(i))
    L1[1] +=1
    print("---------------")
    for i in L1:
        print(id(i))
    print(type(L1), id(L1))
    #Seul l'id 1 de la liste a changer de location ainsi chaque elem = 1 endroit precis
    print("---------------")
    chaine = "machaine"
    for i in chaine:
        print(id(i))
    #Pareil chaque char  = un espace dedié dans la memoire
# exo1()

def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst
lst1 = [0,1,2]
lst2 = ajouter_elt(lst1, len(lst1))
print(lst1, id(lst1), type(lst1))
print(lst2, id(lst2), type(lst2))
#LST1 = LST2 donc leurs id sont egaux...

# Que l'on soit d'accord je sais q'uimporter au milieu du porgramme une librairie n'est pas propre mais comme j'avance avec 1
# Seul document je prefere donc faire comme si a chaque debut d'exos je suis au debut d'un nouveau script
from math import floor
def exo5():
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
exo5()