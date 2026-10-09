base = 4
fromage = 800.0 # = qty de fromage en gramme par personne
eau = 2
ail = 2
pain = 400

nb_ppl = int(input("."))
fromage = fromage*nb_ppl/base
eau = eau*nb_ppl/base
ail = ail*nb_ppl/base
pain = pain*nb_ppl/base
print(f"Fromage en g pour {nb_ppl} personne(s): {fromage}\n* Eau en décilitre {eau}\n* Ail en gousse {ail}\n* Pain en gramme {pain}")