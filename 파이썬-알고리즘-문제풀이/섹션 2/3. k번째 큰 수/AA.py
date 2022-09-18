import sys
#sys.stdin=open("input.txt", "r")
N, K = list(map(int, input().split()))
card = list(map(int, input().split()))

summ = set()
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      summ.add(card[i] + card[j] + card[k])

summ = list(summ)
summ.sort(reverse=True)
print(summ[K-1])