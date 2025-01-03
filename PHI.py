from math import gcd
isCoprime = lambda a, b: gcd(a, b) == 1
n = int(input())
c = 0
for i in range(1, n+1):
    if isCoprime(i, n):
        c += 1
print(c)
