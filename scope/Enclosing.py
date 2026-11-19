def outer():
    x = 100

    def inner():
        # nonlocal x
        x = 50
        print(x)
    inner()

    print(x)


outer()
