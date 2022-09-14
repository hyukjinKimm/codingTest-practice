import sys
sys.stdin=open("input.txt", "r")
N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

count = (M//(K+1))*K
count += M % (K+1)
result = 0
result = result + (count) * arr[N-1]
result = result + (M-count) * arr[N-2]

print(result)