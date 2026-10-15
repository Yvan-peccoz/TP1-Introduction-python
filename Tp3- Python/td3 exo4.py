import random as r

def rdm_game(n=100):
    tbg = r.randint(0,n) #to be guessed is completely rdm
    #print(tbg)
    attempt = 1
    inp_nb = int(input("."))
    while inp_nb != tbg:
        attempt += 1
        if inp_nb > tbg:
            print("<")
        else:
            print(">")
        inp_nb = int(input("."))
    return attempt

print(rdm_game())