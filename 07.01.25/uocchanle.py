def fDiv(n):
    se = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            se.update((i, n//i))
    return sorted(se)

t = int(input())
ans = []
for _ in range(t):
    ans.append("CHAN" if len(fDiv(int(input()))) % 2 == 0 else "LE")
print("\n".join(ans))
