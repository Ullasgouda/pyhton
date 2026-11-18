# 26. Find the maximum occurring character.
st1 = input("Enter the name: ")

maxe = 0
resu = ""

for i in st1:
    count = st1.count(i)

    if count > maxe:
        maxe = count
        resu = i
    elif count == maxe and i not in resu:
        resu += i

print("Maximum occurring character:", resu)
print("Maximum occurrence:", maxe)
