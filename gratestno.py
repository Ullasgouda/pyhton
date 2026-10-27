num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3ed number: "))
if (num1 > num2 and num1 > num3):

    print("Num1 is grate then num2 & num3")
elif (num2 > num1 and num2 > num3):

    print("Num2 is grate then num1 & num3")

elif (num3 > num1 and num3 > num2):

    print("Num3 is grate then num2 & num1")
else:
    print("All number are same ")
