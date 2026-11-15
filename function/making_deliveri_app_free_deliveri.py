# def delveri_app(price, distence=700):
#     if (distence <= 700):
#         return ("You r getting free delivery ")
#     else:
#         return ("you r charged for delivery")
#     print(f"You need to pay {price}RS")


# a = int(input("Enter the price of itme1:"))
# b = int(input("Enter the price of itme2:"))
# c = int(input("Enter the price of itme3:"))
# d = int(input("Enter the price of itme4:"))
# e = int(input("Enter the price of itme5:"))
# f = int(input("Enter the price of itme6:"))
# g = int(input("Enter the price of itme7:"))
# h = int(input("Enter the price of itme8:"))
# price = a+b+c+d+e+f+g+h
# distence = int(input("How far restorent is there from your place "))
# amount = price
# travel = distence

# print(delveri_app(price, distence))

def delivary(price, distance, charge=0,):
    return (f"Your total amount to be paid is {price+charge} and the restorent is {distance}km far from you ")
    if price > 500:
        return f"you got free delivery charge {charge}"

    elif price < 500 and distance < 5:
        return f"you got free delivery charge {charge} because price and distance are less"

    else:
        return f"you got delivery charge {price+charge}"


price = int(input("enter price:"))
distance = int(input("enter distance:"))

amount = 500
travel = 5
if price > amount and distance < travel:
    print(f"You are getting free delivery for ordering more the 500 Rs and the distence from the restorent is less then 5 km from the restorent  ")
    print(delivary(price, distance))
elif price < amount and distance < travel:
    print(
        f"You are getting free delevery for ordering less distence then 5 from the restorent (travling distence is {distance}) ")
    print(delivary(price, distance))
else:
    charge = int(input("enter charge:"))
    print(f"your total amount  is  {price} and charges of {charge}")
    print(delivary(price, distance, charge))
