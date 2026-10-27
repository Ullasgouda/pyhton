num = int(input("ENter the Number  :"))
if (num % 2 == 0 and num % 3 == 0):
    print(f"{num} is div by both 2 and 3")
elif (num % 3 == 0):
    print(f"{num} is div by 3")
elif (num % 2 == 0):
    print(f"{num} is div by 2 ")
else:
    print(f"{num} is not div by both 2 and 3")
