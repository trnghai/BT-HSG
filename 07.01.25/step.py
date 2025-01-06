ans = []
for _ in range(int(input())):
    n = input()
    ans.append("YES" if all(n[i] <= n[i+1] for i in range(len(n)-1)) and len(n) > 1 else "NO")
print("\n".join(ans))
