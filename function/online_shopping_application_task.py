# An online shopping application allows customers to purchase multiple products.

# Task:
# - Create a function shopping_order(customer_name, *prices).
# - Accept customer name as a positional argument.
# - Accept multiple product prices using variable-length arguments.
# - Calculate the total amount.
# - If the total amount exceeds ₹5,000, give a 10% discount.
def shoppinr_order(customer, *price):
    total = sum(price)
    if total > 5000:
        discount = total*0.1
        print(
            f"your are geting dicount your amount was {total} after discount is {total-discount}")
    else:
        print(f"your bill amount is {total}")


name = input("may i know your name sir: ")
order = int(input("how many item did u take sir "))

bill = []

for i in range(0, order):
    price = int(input(f" the price of item{i+1}: "))
    bill.append(price)
shoppinr_order(name, *bill)
