from collections import Counter
import sys

def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

s = input()
c = Counter(s)
nums = tuple(sorted(map(int, ''.join(c if c.isdigit() else " " for c in s).split()), reverse=True))
print(len(c.keys()))
print(c.most_common(1)[0][1])
for i in nums:
    if isPrime(i):
        print(i)
        sys.exit()
print(-1)
