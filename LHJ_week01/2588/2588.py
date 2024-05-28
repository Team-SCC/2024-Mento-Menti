a = int(input())
b = int(input())

c = b % 10
print(a * c)
c = (b % 100) - c
print(int(a * (c / 10)))
c = b - (b % 100)
print(int(a * (c / 100)))
print(a * b)