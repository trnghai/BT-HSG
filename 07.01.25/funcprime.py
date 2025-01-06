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

def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

n = int(input())
print("YES" if isPrime(sum(sieve(2, n))) else "NO")
