from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
c = Counter(s)
print("AC x ", c["AC"])
print("WA x ", c["WA"])
print("TLE x ", c["TLE"])
print("RE x ", c["RE"])