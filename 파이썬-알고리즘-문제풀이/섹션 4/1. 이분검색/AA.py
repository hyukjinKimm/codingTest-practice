import sys
#sys.stdin=open("input.txt", "r")
import bisect
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(bisect.bisect_left(arr, M) + 1) # 3 이상인 값중에 첫번째 
