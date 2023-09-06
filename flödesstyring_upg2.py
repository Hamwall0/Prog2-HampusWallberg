text = input("skriv något ->")
sifror = "0123456789"
antal = 0 
for i in text:
    if i in sifror:
        antal += 1
print(antal)

