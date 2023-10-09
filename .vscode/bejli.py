org = input().split()
rätt = [1,1,2,2,2,8]
fin = ""
for i in range(0,6):
    fin += f" {int(rätt[i])-int(org[i])}"
print(fin)
