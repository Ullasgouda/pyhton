# Write a program to check whether a number is positive and even.
num = int(input("Enter the number to check weather the number is positive and even"))
if (num > 0 and num % 2 == 0):
    print(f"{num} is positive and even ")
elif (num > 0 and num % 2 != 0):
    print(f"{num} is positive but not even")
elif (num < 0 and num % 2 == 0):
    print(f"{num} is even but not positive ")
else:
    print(f"{num} is nither even nor positive ")
