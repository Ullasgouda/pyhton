sent = input("enter the sentens : ")
resu = ""
finel = ""
for i in sent.split():
    leng = len(i)
    if leng > len(resu):
        resu = i
print(resu)
