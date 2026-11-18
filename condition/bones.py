sal = float(input("enter the current salary: "))
exp = float(input("enter the year of experience: "))
if (exp >= 10):
    bones = sal*(20/200)
    print(f"Your got 20% of bones ")
    print(f"your bones amout is {bones}")
elif (exp >= 6):
    bones = sal*(10/100)
    print(f"Your got 10% of bones ")
    print(f"your bones amout is {bones}")
elif (exp >= 2):
    bones = sal*(5/100)
    print(f"Your got 5% of bones ")
    print(f"your bones amout is {bones}")
else:
    print("your dont have enough experines ")
