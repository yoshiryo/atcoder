s = input()
for i in range(len(s)-2, -1, -2):
    t = s[:i]
    mid = i//2
    if t[:mid] == t[mid:]:
        print(i)
        exit()