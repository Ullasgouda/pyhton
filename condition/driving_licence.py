# Write a program to check whether a person is eligible for a driving license
# (age ≥ 18).
num = int(input("Enter your age: "))
id = input("Do you have driving license (yes or no) : ").lower()
if (num >= 18):
    if (id == 'no'):
        print("you can get your license by clearing your driving test ")
    else:
        print("yor alrady have a license")
elif (num <= 18 and id == 'yes'):
    print("you need to get background verification ")
else:
    print("You are not eligible because u r under 18 ")
