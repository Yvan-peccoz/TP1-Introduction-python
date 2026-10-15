def check_val(a, b):
    test = False
    if a >b:
        print("Attention ! le début de la location est après la fin ...")
    elif a==b:
        test = False
        print("Attention ! l’heure de fin est identique à l’heure de début.")
    elif a <0 or a >24 or b <1 or b >25:
        test = False
        print("Les heures doivent être comprises entre 0 et 24 !")
    else:
        test = True
    return test

def locavelo():
    hd = int(input("Donnez l’heure de début de la location (un entier) : "))
    hf = int(input("Donnez l’heure de fin de la location (un entier) : "))
    while check_val(hd, hf) != True:
        hd = int(input("Donnez l’heure de début de la location (un entier) : "))
        hf = int(input("Donnez l’heure de fin de la location (un entier) : "))
    t1 = 0
    t2 = 0
    for i in range(hd, hf):
        if (i >= 0 and i < 7) or (i>16 and i<=24):
            t1 += 1
        else:
            t2 += 1
    tot = t1 +t2*2
    return [t1, t2, tot]
res = locavelo()
if res[0] == 0 and res[1] !=0:
    print(f"{res[1]} heure(s) au tarif horaire de 2.0 euro(s) \nLe montant total à payer est de {res[2]}.0 euro(s).")
elif res[1] == 0 and res[0] !=0:
    print(f"{res[0]} heure(s) au tarif horaire de 1.0 euro(s) \nLe montant total à payer est de {res[2]}.0 euro(s).")
else:
    print(f"{res[0]} heure(s) au tarif horaire de 1.0 euro(s)\n{res[1]} heure(s) au tarif horaire de 2.0 euro(s) \nLe montant total à payer est de {res[2]}.0 euro(s).")