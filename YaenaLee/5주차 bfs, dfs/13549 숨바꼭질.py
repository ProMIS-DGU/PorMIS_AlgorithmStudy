from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int,input().split())
visited = [-1] * 100001
# print(visited)

visited[n] = 0
queue = deque([n])
ans = 0
while(queue):
    first = queue.popleft()
    # print(first)

    dx = [first+1, first-1, first*2]
    for i in dx:
        if i>100000 or i<0:
            continue

        if visited[i] < visited[first] and visited[i]==-1:
            if i == first*2:
                visited[i] = visited[first]
                queue.appendleft(i)

            else:
                visited[i] = visited[first]+1
                queue.append(i)
        if i == k:
            ans = i
            break;

print(visited[ans])