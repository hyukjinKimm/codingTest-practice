import sys
import heapq as hq
sys.stdin=open("input.txt", "r")


def main():
  n = int(input())
  res = list(map(int, input().split()))
  hq.heapify(res)
  for i in range(n-1):
    tmp = list(map(int, input().split()))
    for j in range(n):
      if tmp[j]  > res[0]:
        hq.heappop(res)
        hq.heappush(res, tmp[j])
  print(res[0])

   
if __name__ == "__main__":
  main()
