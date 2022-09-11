import sys
#sys.stdin=open("input.txt", "r")


n, k = map(int , input().split())
arr = list(map(int, input().split()))
card = set()
for i in range(n):
  for j in range(i+1, n):
    for m in range(j+1, n):
      tmp = arr[i] + arr[j] + arr[m]
      card.add(tmp)
card = list(card)
card.sort(reverse=True)
print(card[k-1])

