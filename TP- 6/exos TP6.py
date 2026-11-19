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

def exo5(t):
    t.lower()
    char_delete = ",.!/:;&'"
    char_accent = "éèêëàä"
    char_format= "eeeeaa"
    for i in char_delete:
        t.replace(i,"")
    for i in char_accent:
        t.replace(i,char_format[i])
    print(t)

exo5("Ta bête te bat")