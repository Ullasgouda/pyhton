# 16. Count uppercase, lowercase, digits, and special characters.
sent = input("Enter the sentenceb : ")
countu = 0
countl = 0
countd = 0
counts = 0
for i in sent:
    if (i.isupper()):
        countu += 1

    elif (i.islower()):
        countl += 1

    elif (i.isnumeric()):
        countd += 1

    else:
        counts += 1
print("specal", counts)
print("lower", countl)
print("upper", countu)
print("number", countd)
