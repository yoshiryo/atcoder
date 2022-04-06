n, x = map(int,input().split())
s = input()
t = []
for c in s:
  if c == "U" and len(t) > 0 and (t[-1] == "L" or t[-1] == "R"):
    t.pop()
  else:
    t.append(c)

for c in t:
  if c=="U": 
    x = x//2
  if c=="L":
    x = x*2
  if c=="R": 
    x = x*2 + 1
print(x)