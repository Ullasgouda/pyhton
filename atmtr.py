bal = int(input("Enter the balance in your acc: "))
wd = int(input("Enter the amount you need to take: "))
remaning = (bal-wd)
if (bal >= wd):
    print("You have enter the valid input")
    print(f"your current balance is {remaning} ")
else:
    print("You dont have the balance")
