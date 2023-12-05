a, b, c = 1, 2, 3
print(a, b, c)

zbior = a, b, c
zbior2 = a,
print(zbior)
print(zbior2)
print(zbior[0:2])
x, *y, z = zbior
print(x)
print(y)
print(z)
