import heapq

n = int(input())
array = []
for i in range(n):
    num_list = list(map(int,input().split()))
    for j in range(n):
        heapq.heappush(array,num_list[j])
        if len(array)>n:
            heapq.heappop(array)

print(heapq.heappop(array))
