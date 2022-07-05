import heapq
import sys

n = int(input())
arr = []
end_times = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort()
heapq.heappush(end_times, arr[0][1])

for time in range(1, len(arr)):
    tmp_times = arr[time]
    if arr[time][0] >= end_times[0]:
        heapq.heappop(end_times)

    heapq.heappush(end_times, tmp_times[1])

print(len(end_times))



