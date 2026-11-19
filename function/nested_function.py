def outer():
    print("hi outer")

    def inner():
        print("hi inner")

    return inner()


outer()
