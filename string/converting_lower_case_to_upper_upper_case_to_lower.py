name = input(
    "Enter the name of anything u want to change the upper to lower case and lower to upper case : ")
name1 = ""
for ele in name:
    if ele.isupper():
        name1 += ele.lower()
    else:
        name1 += ele.upper()
print(name1)
