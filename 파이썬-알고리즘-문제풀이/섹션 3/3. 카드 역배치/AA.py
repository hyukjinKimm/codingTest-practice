import sys
#sys.stdin=open("input.txt", "r")

card = [i+1 for i in range(20)]
for i in range(10):
  a, b = map(int, input().split())
  
  for j in range((b-a + 1)//2):
    card[a-1+j], card[b-1-j] = card[b-1-j], card[a-1+j]
for x in card:
  print(x, end = ' ')

