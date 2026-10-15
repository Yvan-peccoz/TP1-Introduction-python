def facto():
    choice = int(input("type 0 for a while loop\n and type 1 for a *for* loop:"))
    while choice != 0 and choice != 1:
        choice = int(input("type 0 for a while loop\n and type 1 for a *for* loop:"))
    n = int(input("Enter a integer:"))
    if choice ==1:
        sum_ = 1
        for i in range(1,n+1):
            sum_ *= i
            print(sum_)
    else:
        sum_ = 1
        while n > 0:
            sum_ *= n
            n-=1
            print(sum_)
    return sum_

facto()