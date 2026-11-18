# write the program on online food delevary app
# 1.accept food item and quantity
# 2.calculate the toatl price
# 3.add 40 rs delivery charge if the order amount is below 500 rs
# 4.disply the finel amount
def onli_food(*item, quntity):
    print(f"You had placed {quntity} items ")
    total = sum(item)
    if (total > 500):
        print(f"Your bill is {total}")
    else:
        print(
            f"Your toatl is {total} and u r getting 40Rs charge for deliveri to total is {total+40}")


item = int(input("Enter the no. of items u took : "))
price1 = []
for i in range(0, item):
    price = int(input("What is the price of item : "))
    price1.append(price)
onli_food(*price1, quntity=item)
