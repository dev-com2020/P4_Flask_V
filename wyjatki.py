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

dane_popsute2 = [
    dict(name='Jan', age='age'),
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
        except ValueError:
            print(f"Niepoprawna wartość {user}")
    return count


# print(check_age(dane, 15))
# print(check_age(dane_popsute, 15))
# print(check_age(dane_popsute2, 15))

def check_age2(users, age):
    count = 0
    for user in users:
        try:
            user_age = int(user['age'])
        except KeyError:
            print(f'Niepoprawne dane {user}')
        except ValueError:
            print(f"Niepoprawna wartość {user}")
        else:
            count += 1 if user_age < age else 0
        finally:
            print(user)
    return count

print(check_age2(dane_popsute2, 15))