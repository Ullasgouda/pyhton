itm1 = int(input("Price of item 1:"))
itm2 = int(input("Price of item 2:"))
itm3 = int(input("Price of item 3:"))
itm4 = int(input("Price of item 4:"))
itm5 = int(input("Price of item 5:"))
itm6 = int(input("Price of item 6:"))
total = itm1+itm2+itm3+itm4+itm5+itm6
print(total)
if (total > 10000):
    print("you are getting 12 off")
    disc = 12
elif (total > 9000 and total < 10000):
    print("you are getting 10 off")
    disc = 10
elif (total > 8000 and total < 9000):
    print("you are getting 9 off")
    disc = 9
elif (total > 7000 and total < 8000):
    print("you are getting 8 off")
    disc = 8
elif (total > 6000 and total < 7000):
    print("you are getting 7 off")
    disc = 7
elif (total > 5000 and total < 6000):
    print("you are getting 6 off")
    disc = 6
elif (total > 4000 and total < 5000):
    print("you are getting 5 off")
    disc = 5
elif (total > 3000 and total < 4000):
    print("you are getting 4 off")
    disc = 4
elif (total > 2000 and total < 3000):
    print("you are getting 3 off")
    disc = 3
elif (total > 1000 and total < 2000):
    print("you are getting 2 off")
    disc = 2
else:
    print("you did't get any off")
    disc = 0
dicount = total*(disc/100)
final = total-dicount
print("your off pricw is ", final)
print(dicount)
