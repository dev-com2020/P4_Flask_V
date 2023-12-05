# pustą listę
osoby = []
osoby.append("Tomek")
osoby.append("ADAM")
osoby.append("Agnieszka")
osoby.append("Szymon")
osoby.append("Dawid")
print(osoby)
print(osoby[0:3])
print(osoby[3:])
print(osoby[:2])
print(osoby[-5:])
print(len(osoby))
osoby.pop()
osoby.remove("Szymon")
osoby.insert(1, "Michał")
print(osoby)

liczby = [1, 3, 5, 7]
liczby_2 = [2, 4, 6]
print(min(liczby))
print(max(liczby))
print(sum(liczby))
lista_3 = liczby + liczby_2
lista_3.sort()
print(lista_3 * 2)
lista_3[0] = 100
lista_3.append(["t", "m", 'j'])
print(lista_3)
print(lista_3[7][1])

