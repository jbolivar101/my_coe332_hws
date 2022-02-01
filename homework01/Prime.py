for x in range(3,101):
    if x>1:
        for i in range(2, x):
            if(x % i == 0):
                break
        else:
            print(x)
