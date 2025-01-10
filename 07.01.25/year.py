n = str(int(input()) + 1)

def isDiff(n):
    if len(set(n)) >= 4:
        return True
    return False

while not isDiff(n):
    n = str(int(n)+1)
print(n)
