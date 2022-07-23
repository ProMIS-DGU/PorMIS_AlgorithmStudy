import sys
import heapq
input = sys.stdin.readline

array = []
n = int(input())
for i in range(n):
    num = int(input())
    if num == 0:
        if not array:
            print(0)
        else:
            ans = heapq.heappop(array)
            if ans[1] == 0:
                print(-ans[0])
            else:
                print(ans[0])
    else:
        if num>0:
            heapq.heappush(array,[num,1])
            # print(array)
        else:
            heapq.heappush(array,[abs(num),0])
            # print(array)
