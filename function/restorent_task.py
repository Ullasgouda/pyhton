# // a restorent owner  alowes coustemer alowes any no. of items eache item has a difrent price .
# // 1.creat a function
# // 2.accept a customer name as positional argument
# // 3. accept any no. of food prices using (* price)
# // 4. calculate the total bill
# // 5. disply the cust name in total amount
def restorent(name, *price):
    total = sum(price)
    print(f"hii {name} , here is your bill amount of {total} ")


name = input("what is your name sir. ")
no_of_order = int(input("how many item did u order sir :"))
bill = []

for i in range(0, no_of_order):
    price = int(input(f" the price of item{i}"))
    bill.append(price)
restorent(name, *bill)
