from pakiet import customers

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
