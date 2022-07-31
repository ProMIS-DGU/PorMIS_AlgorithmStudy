import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [0]*(n+1)
graph = [[]for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        p = queue.popleft()
        for i in graph[p]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(1)
ans = 0
for i in visited:
    if i:
        ans +=1
print(ans-1)