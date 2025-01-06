def fDiv(n):
    se = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            se.update((i, n//i))
    return sorted(se)
    
a, b = map(int, input().split())
d1 = fDiv(a)
d2 = fDiv(b)
del d1[-1], d2[-1]
print("YES" if sum(d1) == b and sum(d2) == a else "NO")
