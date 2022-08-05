import sys
input = sys.stdin.readline
from collections import deque
# N , M ,T 입력받기

N, M, T = map(int, input().split())

graph = []
visited = [[0 for _ in range(M)] for _ in range(N)]

#이동할 방향
dx = [-1,1,0,0]
dy= [0,0,-1,1]

#결과
result=0

# 검을 가지게 될 때 실행될 함수
def bfs2(x, y,t):
    print('여기는 들어옴?')
    queue = deque()
    queue.append((x, y,t))

    while queue:
        x, y,t = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue

        if (graph[ny][nx] < graph[y][x] and graph[ny][nx]!=0) or graph[ny][nx] > graph[y][x]:
            continue

        if graph[ny][nx]==0 or graph[ny][nx]==1:
            graph[ny][nx] = graph[y][x] + 1
            queue.append((nx, ny))
            continue

        if graph[ny][nx] == graph[M-1][N-1]:
            graph[ny][nx] = graph[y][x] + 1
            result = graph[ny][nx]

            return result

# 함수 정의
def bfs(x, y, t):

    queue=deque()
    queue.append((x,y,t))
    visited[y][x] = 1

    while queue:

        print(queue)

        x, y, t= queue.popleft()



        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (t>T):
                print('1')
                result = 'Fail'
                return result

            if ny == (M-1) and  nx == (N-1):
                print('2')
                graph[ny][nx] = graph[y][x] + 1

                result = graph[ny][nx]

                return result

            if nx<0 or ny<0 or nx>=M or ny >=N:
                print('3')

                continue

            if (graph[ny][nx] < graph[y][x]and graph[ny][nx]!=0) or graph[ny][nx] > graph[y][x] :
                print('4')
                continue

            if graph[ny][nx] == 1:
                print('5')
                continue

            if graph[ny][nx]==0:
                print('6')
                visited[ny][nx] == 1
                t = t+1
                graph[ny][nx] = graph[y][x]-1
                queue.append((nx,ny,t))
                continue

            if graph[ny][nx] == 2 and visited[ny][nx] == 0:
                print('7')
                visited[ny][nx] == 1
                t = t + 1
                while queue:
                    queue.popleft()
                bfs2(nx,ny,t)




# miro값 입력받기
for _ in range(M):
    miro = list(map(int, input().split()))
    graph.append(miro)



bfs(0,0,0)

print('답은 말이죠')
print(result)
if (result<T):
    print('Fail')
else:
    print(result)

