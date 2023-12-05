liczba = 200
imie = "Tomek"
osoba = "Michał"
wersja = 3.10

print(f"Liczba uczestników wynosi {liczba}, a prowadzącym jest {imie}")
print("Aktywny uczestnik to {0}, a czas prelekcji to {1} minut".format(osoba, liczba))
print("Aktywny uczestnik to %s, a czas prelekcji to %d minut" % (imie, liczba))
print("Używamy wersji Python %i" % wersja)
print("Używamy wersji Python %f" % wersja)
print("Używamy wersji Python %.2f" % wersja)
print(f"Używamy wersji Python {wersja:.2f}")
print("Używamy wersji Python {:.2f}".format(wersja))
