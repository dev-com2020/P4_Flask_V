spoznienie = False

if spoznienie:
    print("Dzwonię do szefa!")
else:
    print("Nie muszę nigdzie dzownić!")

przychod = 15000
if przychod < 10000:
    podatek = 0.0
elif przychod < 30000:
    podatek = 0.2
elif przychod < 100000:
    podatek = 0.35
else:
    podatek = 0.45

print("Zapłciłem podatku:", przychod * podatek)

alert_system = 'console5'

if alert_system == 'console':
    print("Błąd!!")
    if przychod > 10000:
        print("Twój przychód jest duży")

zam_total = 1200

if zam_total > 999:
    rabat = 10
else:
    rabat = 0

print(zam_total, rabat)

rabat = 10 if zam_total > 999 else 0
print(zam_total, rabat)
