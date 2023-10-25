Ttid = 18
Tmo = 0
Mmo = 0
Mtid = 19
antal = 40
i = 0
while antal > 0:
    if antal == 1 and i % Ttid == 0 and i % Mtid == 0:
        break

    if i % Ttid == 0:
        Tmo += 1
        antal -= 1

    if i % Mtid == 0:
        Mmo += 1
        antal -= 1
    i += 1
print(f"Thor {Tmo}")
print(f"mor {Mmo}")
