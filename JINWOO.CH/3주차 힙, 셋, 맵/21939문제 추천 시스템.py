import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []
max_heap = []

for i in range(N):
    P, L = map(int, input().split())
    heapq.heappush(min_heap, (L,P))
    heapq.heappush(max_heap, (-L,-P))

print(min_heap)
print(max_heap)

# M= int(sys.stdin.readline())
#
# for a in range(M):
#     order =input().split()
#     if(order[0]=='recommend'):
#         if(order[1]=='1'):




