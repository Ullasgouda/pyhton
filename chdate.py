date = int(input("Enter the date  :"))
month = int(input("Enter the month :"))
year = int(input("Enter the year  :"))
if (month >= 1 and month <= 12):
    if (month == 2):
        if (year % 4 and year % 100 != 0):
            day = 29
        else:
            day = 28
    if (month == [4, 6, 8, 10, 12]):
        day = 30
    else:
        day = 31
    if (date > 1 and date < day):

        print("valid Date")
    else:
        print("Invaid Date")
else:
    print("Invalid Month")
