num = int(input("enter your no."))
i = 2
c = 0
if (num <= 1):
    print("not prime no.")
else:
    while (i <= num/2):
        if (num % i == 0):
            c = c + 1
            break
        i += 1

    if (c == 0):
        print("prime no.")
    else:
        print("not prime no.")
