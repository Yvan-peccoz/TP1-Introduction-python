user = int(input("."))
# 60 * 24 (nb min par heure * nb heure par jour)
j = user//1440 # essentielment l'inverse que l'exo d'avant
h = (user%1440)//60
m = ((user%1440)%60)
print(f"{j}:{h}:{m}")

