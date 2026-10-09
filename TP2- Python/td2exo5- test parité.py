inp = int(input("Entrez un nombre entier :"))
if inp == 0:
    print("Le nombre est zéro (et il est pair)")
elif inp % 2 == 0:
    if inp >0:
        print("positif et paire")
    else:
        print("negatif et paire")
else:
    if inp >0:
        print("positif et impaire")
    else:
        print("negatif et impaire")
