def outer():
    x=20
    print(x)
    def inner():
        y=30
        print(x) ### It is Used in Nested Function
        return
    inner()
outer()
