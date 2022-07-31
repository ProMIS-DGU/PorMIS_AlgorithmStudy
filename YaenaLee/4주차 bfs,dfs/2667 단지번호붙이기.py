from collections import deque
graph = []
n = int(input())
for i in range(n):
    l = list(map(int,input()))
    graph.append(l)
# print(graph)
visited = [[False for i in range(n)]for i in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(a,b):
    count = 1
    queue = deque([[a,b]])
    visited[a][b] = True

    while queue:
        # print(queue)
        pop = queue.popleft()
        x = pop[0]
        y = pop[1]
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if new_x<0 or new_y<0 or new_x>=n or new_y>=n:
                continue
            if graph[new_x][new_y] == 1 and not visited[new_x][new_y]:
                queue.append([new_x,new_y])
                count +=1
                visited[new_x][new_y] = True
    return count
ans = 0
cnt_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            ans+=1
            cnt_list.append(bfs(i,j))


print(ans)
cnt_list.sort()
for i in range(ans):
    print(cnt_list[i])