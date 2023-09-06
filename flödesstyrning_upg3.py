prime = [2,3,5,7,11]
tusen_prime = []
tal = 1
while len(prime) < 1000:
    for i in prime:
        if tal % i == 0:
            tal+= 1
            break
        else:
            prime.append(tal)
            tal += 1
            break
            
print(prime)
print(prime[-1])
            

        
    
