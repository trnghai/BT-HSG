a, b = input().split()
s = 0
for i in a:
    for j in b:
        s += int(i) * int(j)
print(s)
