import pakiet
from pakiet import *
from pakiet import coupons

customers = (1, 2, 3)
wyniki_vat = []

print(pakiet.customers[0]['code'])
print(customers)
coupons.drukuj_rabat()
wynik23 = coupons.calculate_vat(1000, 23)
wynik8 = coupons.calculate_vat(1000, 8)
wynik0 = coupons.calculate_vat(1000, 0)
wynik2 = coupons.calculate_vat(1000)
print("Vat 23=", wynik23)
print("Vat 8=", wynik8)
print("Vat 0=", wynik0)
print("Vat 2=", wynik2)
wyniki_vat.append(wynik23)
wyniki_vat.append(wynik8)
wyniki_vat.append(wynik0)
wyniki_vat.append(wynik2)
print(wyniki_vat)
