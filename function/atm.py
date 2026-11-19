# Create an outer function atm() with an initial balance of ₹25,000.

# Inner functions:
# - PIN verification
# - Cash withdrawal
# - Balance enquiry
# - Mini statement
def atm():
    bal = int(input("Enter the balence :"))
    if bal > 25000:

        def detail():
            pin = int(input("Enter the pin : "))
            csah = int(input("enter how much cash do u want to withdrawal: "))
            balens = (bal-csah)
            if (len(str(pin)) == 4):
                print("valid ")
            else:
                print("Invalid")
            print("Banlense ofter withdrowal", balens)
        detail()
    else:
        print("invalid balence ")


atm()
