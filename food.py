#  write a program nested if-else of a online food ordering system
# ask the user wether they order food
# if yes ask for the food price
# if the prise aclist 500 ask weather the user had the copen
# if they have a copen apply a 10%discont otherwise charge the full amount
# if the user dont want to order print order calcled
itm1 = int(input("1.enter the price of the item you are buying: "))
itm2 = int(input("2.enter the price of the item you are buying: "))
itm3 = int(input("3.enter the price of the item you are buying: "))
itm4 = int(input("4.enter the price of the item you are buying: "))
price = itm1+itm2+itm3+itm4
ask = input("Hi,sir/madam\n do you want to order somthing (yes or no): ").lower()

if (ask == 'yes'):

    if (price >= 500):
        copen = input("Do u have any coupon (yes or no): ")

        if (copen == 'yes'):
            print(f"You r geting 10% OFF on your food")
            print(f"your need pay {price-price*(10/100)} ")
            print(f"your r geting discont of {price*(10/100)}")
            order = input("Do you want to orde(yes or no): ").lower()

        else:
            print(f"your total amount is {price}")
            order = input("Do you want to orde(yes or no): ").lower()

        if (order == 'yes'):
            print(f'order placed')
        else:
            print(f'order cancled')
    else:
        print("for this amount order cant be palced")
else:
    print("Thank you sir/madam ")
