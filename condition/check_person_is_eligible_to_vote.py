# . Write a program to check whether a person is eligible to vote (age ≥ 18).
num = int(input("Enter your age: "))
id = input("Do you have voter ID (yes or no) : ").lower()
if (id == "yes"):
    if (num >= 18):
        print("you are eligible to vote ")
else:
    print("You are not eligible to vote ")
