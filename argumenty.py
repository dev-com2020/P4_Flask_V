def duzo_rzeczy(*args, **kwargs):
    print(args)
    print(kwargs)


duzo_rzeczy()
duzo_rzeczy(12, 32, 45, 65)
duzo_rzeczy(imie="Tomek", wiek=40)
duzo_rzeczy(12, 32, 45, 65, imie="Tomek", wiek=40)
