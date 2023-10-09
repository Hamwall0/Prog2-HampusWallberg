def add_this(*tal):
    summa = 0
    for i in tal:
        summa += i 
    return summa
print(add_this(1,2,5))

def food (s,vegan=False):
    if vegan:
        print(f"soja{s}")
    else:
        print(s)
food("mjölk",True)