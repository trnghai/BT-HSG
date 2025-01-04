a, b, c = map(float, input().split())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"{(a*b*c)/(4*S):.2f}")
