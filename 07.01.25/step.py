for _ in range(int(input())):
    n = input()
    print("YES" if all(n[i] <= n[i+1] for i in range(len(n)-1)) and len(n) > 1 else "NO")
