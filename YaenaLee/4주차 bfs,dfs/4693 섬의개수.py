import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]


while(True):
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        l = list(map(int,input().split()))
        graph.append(l)
    # print(graph)
    count = 0
    visited = [[False for _ in range(w)]for _ in range(h)]
    # print(visited)
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]==1:
                queue = deque([[i,j]])
                visited[i][j] = True
                count += 1
                while queue:
                    pop = queue.popleft()
                    x = pop[0]
                    y = pop[1]
                    for z in range(8):
                        new_x = x + dx[z]
                        new_y = y + dy[z]

                        if new_x <0 or new_y<0 or new_x>=h or new_y>=w:
                            continue
                        if graph[new_x][new_y]==1 and not visited[new_x][new_y]:
                            queue.append([new_x,new_y])
                            visited[new_x][new_y] = True

    print(count)





