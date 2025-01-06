n = int(input())
while True:
    if str(n) == str(n)[::-1]:
        print(n)
        break
    n += int(str(n)[::-1])
