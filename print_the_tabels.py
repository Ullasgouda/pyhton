num = int(input("Enter a number: "))
temp = num
for num in range(1, 11, 1):
    print(f"{temp} x {num} = {temp*num}")
else:
    print("Done")
