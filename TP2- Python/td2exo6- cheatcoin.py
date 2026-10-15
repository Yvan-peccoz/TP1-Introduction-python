from random import randint
def fairlaunch():
    test = "face"
    coin = randint(1, 100)
    if coin < 50:
        test = "pile"
    return test

#exo n° 7 :
def riggedlaunch_(param):
    test = "face"
    coin = randint(1, param)
    if coin >=1 and coin <param:
        test = "pile"
    return test

print(fairlaunch(),"\n ------")
print(riggedlaunch_(3))