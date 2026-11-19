# Create an outer function calculate() and an inner function addition().

# - Accept two numbers in the outer function.
# - Perform addition inside the inner function.
# - Display the result.
def caluclate():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))

    def add():
        return num1+num2
    return add()


print(caluclate())
1
