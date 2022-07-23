import heapq
import sys

input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    num = int(input())
    if num == 0 and array:
        res = heapq.heappop(array)
        print(-res)
    elif num == 0 and not array:
        print(0)
    else:
        heapq.heappush(array,-num)
