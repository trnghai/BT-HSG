a, b, c = map(float, input().split())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"{S/p:.2f}")
