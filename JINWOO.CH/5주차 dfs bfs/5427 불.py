from collections import deque

# x = int(input())

w, h = map(int, input().split())

graph = []
visited = [[False]*w for _ in range(h)]
fire=deque()
people=deque()
t=0
#이동할 방향
dx = [-1,1,0,0]
dy= [0,0,-1,1]

for _ in range(h):
    building = list(input().rstrip())
    graph.append(building)

for i in range(h):
    for j in range(w):
            if (graph[i][j] == '#'):
                visited[i][j] = True # True == 벽
            elif (graph[i][j] == '*'):
                fire.append((j, i))
            elif (graph[i][j] == '@'):
                people.append((j, i))

# fire x, y  값 받아오기  x==fire[0][0] y=fire[0][1]
def  bfs(fire,people):

    x = fire[0][0]
    y = fire[0][1]

    a = people[0][0]
    b = people[0][1]

    #visited 체크
    visited[y][x] = True

    while fire & people:
        #queue에서 빼기
        x,y = fire.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>w-1 or ny>h-1 or nx<0 or ny<0 :
                continue

            if visited[ny][nx]==False:
                visited[ny][nx] = True
                fire.append((nx,ny))

        #사람
        a, b = people.popleft()
        t = t + 1

        for j in range(4):
            na = a + dx[j]
            nb = b + dy[j]

            if visited[nb][na] == True:
                continue

            if na > w - 1 or nb > h - 1 or na < 0 or nb < 0:
                continue

            if visited[nb][na] == False:
                visited[nb][na] = True
                people.append((na, nb))
