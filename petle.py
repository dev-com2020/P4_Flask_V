liczby = [1, 3, 5, 7]

for liczba in liczby:
    if liczba == 5:
        print(liczba * 100)
    else:
        print(liczba)

osoby = ["Tomek", "Ania", 'Adam']
for pozycja in range(len(osoby)):
    print(pozycja, osoby[pozycja])

osoby = ["Tomek", "Ania", 'Adam']
for pozycja, imie in enumerate(osoby):
    print(pozycja, imie)

wiek = [23, 33, 26]
for pozycja in range(len(osoby)):
    osoba = osoby[pozycja]
    age = wiek[pozycja]
    print(osoba, age)

for person, age in zip(osoby, wiek):
    print(person, age)


