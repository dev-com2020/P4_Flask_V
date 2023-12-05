from pakiet import customers


def drukuj_rabat():
    print(customers)

    for customer in customers:
        code = customer['code']
        if code == 'f20':
            customer['discount'] = 20.0
        elif code == 'f40':
            customer['discount'] = 15.0
        else:
            customer['discount'] = 0.0

    for customer in customers:
        print(customer['id'], " | ", customer['total'], " | ", customer['discount'])


def calculate_vat(price, vat=2):
    return price * (100 + vat) / 100
