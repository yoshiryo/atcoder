n, k = map(int, input().split())
d = set(list(input().split()))
for i in range(n, 88889):
    num_s = list(str(i))
    judge = True
    for j in range(len(num_s)):
        if num_s[j] in d:
            judge = False
            break
    if judge:
        print(i)
        exit()