def sieve(l, r):
    limit = int(r**0.5) + 1
    base = [True] * limit
    base[0] = base[1] = False
    for i in range(2, limit):
        for j in range(i*i, limit, i):
            base[j] = False
    primes = [i for i in range(2, limit) if base[i]]
    sieve = [True] * (r - l + 1)
    for p in primes:
        for j in range(max(p*p, (l+p-1)//p*p), r+1, p):
            sieve[j-l] = False
    final = [i for i in range(l, r+1) if sieve[i-l]]
    return final

def gen(s):
    s = str(s)
    o = s
    se = set()
    while True:
        s = s[1:] + s[0]
        se.add(int(s))
        if s == o:
            return se
          
n = int(input())
primes = set(sieve(2, n-1))
c = 0
for p in primes:
    if gen(p) <= primes:
        c += 1
print(c)
