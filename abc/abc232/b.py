s = input()
t = input()
A = [ord(char) - ord('a') for char in s]
B = [ord(char) - ord('a') for char in t]
for k in range(26):
    C = [(x + k) % 26 for x in A]
    if B == C:
        print("Yes")
        exit()
print("No")
