n = int(input())
w = [input() for _ in range(n)]
if len(set(w)) == n:
    for i in range(n-1):
        now = w[i]
        next = w[i+1]
        if now[-1] != next[0]:
            print("No")
            exit()
    print("Yes")
else:
    print("No")
