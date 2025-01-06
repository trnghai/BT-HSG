a, b = map(int, input().split())
c, d = map(int, input().split())
t = a*d - b*c
m = b*d
for i in range(min(abs(t), abs(m)), 0, -1):
    if t % i == 0 and m % i == 0:
        t //= i
        m //= i
        break

if t < 0 and m < 0:
    print(f"{-t}/{-m}")
elif m < 0:
    print(f"-{t}/{-m}")
else:
    print(f"{t}/{m}")
