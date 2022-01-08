import collections
q = int(input())
cards = collections.deque()
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        cards.appendleft(x)
    elif t == 2:
        cards.append(x)
    else:
        print(cards[x-1])
