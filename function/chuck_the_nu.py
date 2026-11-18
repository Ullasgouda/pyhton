# chucke the given phone no. is valid or invalid
def phone_num(contry, number):
    if contry in ('+91', '+92', '+1', '+44', '+61',
                  '+223', '+233', '+33', '+260', '+237', '+27'):

        if len(str(number)) == 10:
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")


country1 = input(
    "which country are your from give the code like (+19,+92,+1,+44,+61,+223,+233,+33,+260,+237,+27): ")
phone1 = int(input("enter your number "))
phone_num(contry=country1, number=phone1)
