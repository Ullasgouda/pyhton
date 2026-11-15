name = input("enter the name : ")
maxe = 0
stre = ""
for ele in name:
    count = 0
    for i in name:
        if ele == i:
            count += 1
    if count > maxe:
        maxe = count
        stre = ele
print(maxe)
print(stre)
