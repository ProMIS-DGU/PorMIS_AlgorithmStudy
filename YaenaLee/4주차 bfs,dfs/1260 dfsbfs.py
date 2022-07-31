import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int,input().split())
visited = [False] * (n+1)
visited2 = [False] * (n+1)
graph = [[] for i in range (n+1)]


for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
# print(graph)
dfs_ans = []
def dfs(x):
    dfs_ans.append(x)
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

queue = deque([v])
bfs_ans = []
while queue:
    a = queue.popleft()
    bfs_ans.append(a)
    visited2[a] = True
    for i in graph[a]:
        if not visited2[i] :
            queue.append(i)
            visited2[i] = True



dfs(v)
print(*dfs_ans)
print(*bfs_ans)
