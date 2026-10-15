"""Dans ce programme le but est d'interchanger les valeurs de 2 variables"""

va = int(input("."))
vb = int(input("."))
vc = int(input("."))
vt = va
va = vc
vc = vb
vb = vt
print(f"Variable n°1 :{va} \nVariable n°2 :{vb} \nVariable n°3 :{vc}")