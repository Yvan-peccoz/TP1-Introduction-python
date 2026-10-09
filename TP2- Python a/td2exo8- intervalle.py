x = float(input("Pls input a reel number:"))
if ((x >=2 and x<3) or (x>0 and x<=1))or (x>=-10 and x<=-2):
    print(f"{x} appartient à l'ensemble [2,3[ U ]0,1] U [-10,-2]")
else:
    print(f"{x} n'appartient pas à l'ensemble [2,3[ U ]0,1] U [-10,-2]")