card = list(map(int, input().split()))
card.sort(reverse=True)
print(card[0] + card[1])
