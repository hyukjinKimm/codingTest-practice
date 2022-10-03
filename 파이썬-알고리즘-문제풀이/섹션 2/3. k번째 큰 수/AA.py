import sys
#sys.stdin=open("input.txt", "r")
N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = set()
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      ans.add(cards[i] + cards[j] + cards[k])
print(sorted(ans, reverse=True)[M-1])
    