test = 0

def moja_f():
    global test
    test = 1
    def inner():
        # global test
        test = 2
        print("INNER:", id(test))
    inner()
    print("Moja funkcja:", id(test))

moja_f()
print("Globalny:", id(test))
