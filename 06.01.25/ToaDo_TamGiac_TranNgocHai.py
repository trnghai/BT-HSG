import sys

A, B, C = [tuple(map(int, input().split())) for _ in range(3)]
dist = lambda A, B: ((A[0]-B[0])**2+(A[1]-B[1])**2)**0.5
a = dist(B, C)
b = dist(A, C)
c = dist(A, B)
tu = tuple(sorted((a, b, c), reverse=True))
floatEqual = lambda x, y: abs(x-y) <= 1e-8

if not all((a < b + c, b < a + c, c < a + b, a - b < c, a - c < b, b - c < a)):
    print("Không là tam giác")
    sys.exit()

if floatEqual(a, b) and floatEqual(b, c) and floatEqual(a, c):
    print("Tam giác đều")
elif all((floatEqual(tu[1], tu[2]), floatEqual(tu[0]**2, tu[1]**2+tu[2]**2))):
    print("Tam giác vuông cân")
elif floatEqual(tu[1], tu[2]):
    print("Tam giác cân")
elif floatEqual(tu[0]**2, tu[1]**2+tu[2]**2):
    print("Tam giác vuông")
elif tu[0]**2 > tu[1]**2 + tu[2]**2:
    print("Tam giác tù")
else:
    print("Tam giác nhọn")
