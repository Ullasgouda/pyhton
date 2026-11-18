sent = input("Enter the sentense : ")
resul = ""
for i in sent:
    if i == " ":
        resul += "$"
    else:
        resul += i
print(resul)
