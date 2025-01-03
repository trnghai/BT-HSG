def sieve(l, r):
    size = r + 1
    base = [True] * size
    base[0] = base[1] = False
    for i in range(2, int(size**0.5)+1):
        if base[i]:
            for j in range(i*i, size, i):
                base[j] = False
    primes = tuple(x for x in range(2, size) if base[x])
    sieve = [True] * (r-l+1)
    for p in primes:
        for j in range(max(p*p, (l+p-1)//p*p), size, p):
            sieve[j-l] = False
    if l <= 1:
        sieve[1-l] = False
    return tuple(x for x in range(l, size) if sieve[x-l])

li = []
n = int(input())
primes = sieve(2, int(n**0.5))
for p in primes:
    pow = 0
    while n % p == 0:
        pow += 1
        n //= p
    li.append((p, pow))


for pair in li:
    if pair[1] != 0:
        print(f"{pair[0]}^{pair[1]}")
