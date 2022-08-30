import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N) :
    x = int(sys.stdin.readline())

    if x>0 :
        heapq.heappush(heap,(-1)*x) #마이너스를 붙여주면 값이 클수록 작으니까
    else:
        if len(heap)==0:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))




