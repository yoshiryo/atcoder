import bisect
import array

l, q = map(int, input().split())
L = array.array("i", [0, l])
for i in range(q):
    c, x = map(int, input().split())
    if c == 1:
        bisect.insort(L, x)
    else:
        right = bisect.bisect_right(L, x)
        left = right - 1
        diff = L[right] - L[left]
        print(diff)