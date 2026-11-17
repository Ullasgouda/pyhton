def hotel_bill(*price):
    return (f"{sum(price)} is the total bill u need to pay ")


print(hotel_bill(10, 20, 30, 40, 50))
