antal_block = input()

i = 1 
höjd = 0
while antal_block >= i**2:
    antal_block -= i**2
    i += 2
    höjd += 1

print(höjd)