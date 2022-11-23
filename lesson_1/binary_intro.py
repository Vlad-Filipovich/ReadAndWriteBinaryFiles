x = 127
print(1 * pow(10, 2) + 2 * pow(10, 1) + 7 * pow(10, 0))

y = 0b0011
print(0*pow(2,3) + 0 * pow(2, 2) + 1 * pow(2, 1) + 1 * pow(2, 0))
print(y)

y1 = 0b101
print(1 * pow(2, 2) + 0 * pow(2, 1) + 1 * pow(2, 0))
print(y1)

z = 0x2cf1
print(2 * pow(16, 3) + 12 * pow(16, 2) + 15 * pow(16, 1) + 1 * pow(16, 0))
print(z)

z1 = 0x111
print(1 * pow(16, 2) + 1 * pow(16, 1) + 1 * pow(16, 0))
print(z1)

z2 = 0xffff
print(15 * pow(16, 3) + 15 * pow(16, 2) + 15 * pow(16, 1) + 15 * pow(16, 0))
print(z2)
print(format(z2, 'b'))

print(0b1111111111111111)