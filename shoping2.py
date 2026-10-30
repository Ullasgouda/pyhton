itm1 = int(input("Price of item 1:"))
itm2 = int(input("Price of item 2:"))
itm3 = int(input("Price of item 3:"))
itm4 = int(input("Price of item 4:"))
itm5 = int(input("Price of item 5:"))
itm6 = int(input("Price of item 6:"))
total = itm1+itm2+itm3+itm4+itm5+itm6
if (total > 5000):
    if (total > 12000):
        print(f"You got 15% OFF on your shopping")
        disc = 15
    elif (total > 8000 and total <= 12000):
        print(f"You got 12% OFF on your shopping ")
        disc = 12
    elif (total > 5000 and total <= 8000):
        print(f"You got 10% OFF on your shopping ")
        disc = 10
else:
    print("thank you for shoping ")

dicount = total*(disc/100)

print(f"Pay {dicount} RS")
print(disc)
