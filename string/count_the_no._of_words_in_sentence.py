name = input("enter the sentence : ")
name1 = name.strip()
coutn = 1
for i in name1:
    if i == " ":
        coutn += 1

print(coutn)
