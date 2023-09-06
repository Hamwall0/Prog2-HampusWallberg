import math 
count = 0 
prime = [2,3,5,7,11]
tal = 12
while  len(prime) < 1000: 
    check = 1
    while math.sqrt(tal) >= check:
        if tal % check == 0:
            check += 1
            continue
        else:
            prime.append(tal)
            # print("hej")
            break
    tal += 1
print(prime)
# print(prime)
