import sys
input = sys.stdin.readline
from collections import deque
# N , M ,T 입력받기

N, M, T = map(int, input().split())
graph = []
visited = [[0 for _ in range(M)] for _ in range(N)]

# miro값 입력받기
for _ in range(M):
    miro = list(map(int, input().split()))
    graph.append(miro)

#이동할 방향
dx = [-1,1,0,0]
dy= [0,0,-1,1]

#결과
result=0

# 검을 가지게 될 때 실행될 함수
def bfs2(x, y,t):
    queue = deque()
    queue.append((x, y, t))

    while queue:
        x, y,t = queue.popleft()

        if (t > T):
            result = 'Fail'
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny == (M - 1) and nx == (N - 1):
                graph[ny][nx] = graph[y][x] + 1

                result = graph[ny][nx]
                break

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if (graph[ny][nx] < graph[y][x] and graph[ny][nx]!=0) or graph[ny][nx] > graph[y][x]:
                continue

            if (graph[ny][nx]==0 and visited[ny][nx]==0) or (graph[ny][nx]==1 or  visited[ny][nx]==0):
                visited[ny][nx] = 1
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny, graph[ny][nx]))


# 함수 정의
def bfs(x, y, t):

    queue=deque()
    queue.append((x,y,t))
    visited[y][x] = 1



    while queue:
        print(t)
        print(queue)
        x, y, t= queue.popleft()

        if (t > T):
            result = 'Fail'
            break

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if ny == (M-1) and  nx == (N-1):
                graph[ny][nx] = graph[y][x] + 1

                result= graph[ny][nx]

                break

            if nx<0 or ny<0 or nx>=N-1 or ny >=M-1:

                continue

            if graph[ny][nx] == 1:
                continue

            if graph[ny][nx] == 2 and visited[ny][nx] == 0:
                print('와우우우')
                visited[ny][nx] = 1
                graph[ny][nx] = graph[y][x] + 1
                while queue:
                    queue.popleft()
                bfs2(nx,ny,graph[ny][nx])

            if graph[ny][nx] == 0 and visited[ny][nx]!=1:
                visited[ny][nx] = 1
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny, graph[ny][nx]))




bfs(0,0,0)

print(result)

