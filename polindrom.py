num = int(input("entr the number : "))
num2 = 0
while (num > 0):
    i = num % 10
    num2 = num2*10 + i
    num //= 10
    num == num2
if (num2 == num):
    print("Given nuber is palindrom ")
else:
    print("Given nuber is not a palindrom")
