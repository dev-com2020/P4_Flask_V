def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        return 0


def mnozenie2(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        return 0


def mnozenie3(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        return "błąd:", e


# print(mnozenie('a', 'b'))
# print(mnozenie2('a', 'b'))
# print(mnozenie3('a', 'b'))


dane = [
    dict(name='Jan', age='10'),
    dict(name='Dawid', age='19'),
    dict(name='Marcin', age='17'),
]

dane_popsute = [
    dict(),
    dict(name='Dawid', age='19'),
    dict(name='Marcin', age='17'),
]


def check_age(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except KeyError:
            print(f'Niepoprawne dane {user}')
    return count


print(check_age(dane, 15))
print(check_age(dane_popsute, 15))