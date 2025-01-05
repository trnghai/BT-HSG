n = int(input())
a = tuple(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    if a[i] > a[i-1]:
        dp[i] += dp[i-1]
s = sum(i for i in a if (i % 2 == 1) and (i > 0))
print(s)
print(max(dp))
