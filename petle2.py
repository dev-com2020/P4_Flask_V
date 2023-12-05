osoby = ["Tomek", "Ania", 'Adam']
wiek = [23, 33, 26]

# pozycja = 0
# while pozycja < len(osoby):
#     person = osoby[pozycja]
#     age = wiek[pozycja]
#     print(person, age)
#     pozycja += 1  # pozycja = pozycja + 1

while True:
    menu = input("1.wyświetl tablicę wiek,\n2.wyświetl tablicę osoby,\n3.wyjdź z programu ")
    if menu == '1':
        print(wiek)
    elif menu == '2':
        print(osoby)
    else:
        break

