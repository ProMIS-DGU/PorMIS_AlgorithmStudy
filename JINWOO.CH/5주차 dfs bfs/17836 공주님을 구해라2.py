import sys
input = sys.stdin.readline
from collections import deque

# 숫자 받아오기
n, m, t = map(int, input().split())

# 성의 구조 받아오기
graph = []
for _ in range(m):
    miro = list(map(int, input().split()))
    graph.append(miro)

visited = [[False]*n for _ in range(m)]


#이동방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#값
global result1 #검 가지기 전까지 이동수
result1=0
global result2 #검 가지기 나서 이동수
result2=0
global end
end=''

def bfs2(x , y, z):

    queue2 = deque()
    visited[y][x] = True
    queue2.append((x, y, z))
    global end

    while queue2 and end=='':
        x, y, z = queue2.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue

            if (graph[ny][nx] == 0 or graph[ny][nx] == 1) and visited[ny][nx] == False:
                z = graph[y][x] + 1
                graph[ny][nx] = z
                visited[ny][nx] = True
                queue2.append((nx, ny, z))

            if graph[ny][nx] == 2 and visited[ny][nx] == False:
                global result2
                result2=z
                if (result1 + result2 + 2) > t:
                    print('Fail')
                else:
                    print(result1 + result2 + 2)
                end='end'
                break
    if (result2 == 0):
        print('Fail')


def bfs(x, y, z):

    queue = deque()
    visited[y][x]=True
    queue.append((x,y,z))

    while queue:
        x, y, z = queue.popleft()

        if z>t :
            print('Fail')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                continue

            if graph[ny][nx] == 0 and visited[ny][nx]==False:

                z=graph[y][x]+1
                graph[ny][nx] = z
                visited[ny][nx]=True
                queue.append((nx,ny,z))

            if graph[ny][nx] == 2 and visited[ny][nx]==False:
                global result1
                result1=z
                bfs2(n-1,m-1,0)

    if (result1 == 0):
        print('Fail')

bfs(0,0,0)
