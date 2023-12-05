test = 0

def moja_f():
    global test
    test = 1
    print("Moja funkcja:", test)

moja_f()
print("Globalny:", test)
