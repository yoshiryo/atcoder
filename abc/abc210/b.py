n = int(input())
s = input()

for i in range(n):
    if s[i] == "1":
        bad = i+1
        break
if bad % 2 == 0:
    print("Aoki")
else:
    print("Takahashi")