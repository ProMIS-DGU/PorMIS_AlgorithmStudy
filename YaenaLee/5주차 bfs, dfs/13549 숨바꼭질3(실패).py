import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
queue = deque([n])

visited = [-1]*100000
visited[n] = 0
while queue:

    x = queue.popleft()
    # print(x)
    dx = [x,1,-1]
    for i in dx:
        new_x = x+i
        # print(new_x)
        if new_x <0 or new_x>=100000 or visited[new_x]!=-1:
            continue

        if i == x:
            queue.append(new_x)
            visited[new_x] = visited[x]

        if i!= x :
            queue.append(new_x)
            visited[new_x] = visited[x]+1

        if new_x == k:
            print(visited[new_x])
            break

