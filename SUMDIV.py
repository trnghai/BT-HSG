n = int(input())
se = set()
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        se.update((i, n//i))
print(sum(se))
