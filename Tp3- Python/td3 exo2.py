# Exo 1 :
def exo2_1():
    n = int(input("."))
    sum_ = 0
    for i in range(n+1): sum_ += i
    return(sum_)

def exo2_2(nb = 100):
    n=int(input("."))
    while n != nb:
        n=int(input("."))
    return(True)

def exo2_3(nb=10):
    _tmp = []
    for _i in range(nb):
        _tmp.append(int(input(".")))
    int1, int2, int3 = 0,0,0
    for j in _tmp:
        if j <= 10:
            int1 += 1
        elif j >= 15:
            int3 += 1
        else:
            int2 += 1
    return(int1, int2, int3)

def exo2_4():
    x = int(input("."))
    i = 0
    sum_ = 0
    res = None
    while i <= x:
        i += 1
        sum_ += i
        if sum_ <= x:
            res = sum_
        else:
            return res

print(exo2_4())