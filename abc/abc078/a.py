x, y = input().split()
alp = "ABCDEF"
if x == y:
    print("=")
elif alp.find(x) > alp.find(y):
    print(">")
else:
    print("<")