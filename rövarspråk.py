konsonanter = "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, z"
ord = input("Skriv något->")
rövare = ""
for i in ord:
    print(i)
    if i.lower() in konsonanter:
        rövare += f"{i}o{i}"
    else:
        rövare += i

print(rövare)
