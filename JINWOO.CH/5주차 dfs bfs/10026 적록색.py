import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#숫자 입력
N = int(input().rstrip())

#색 입력받기
graph= []
for _ in range(N):
    color = list(input().rstrip())
    graph.append(color)

#이동할 방향
dx = [-1,1,0,0]
dy= [0,0,-1,1]


visited = [[0]*N for _ in range(N)]
result = 0
result2 = 0


# dfs 함수 정의

def dfs(x, y):
    visited[y][x]=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if  nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
            continue

        if graph[y][x]==graph[ny][nx] and visited[ny][nx] == 0:

            dfs(nx, ny)

# 적록색약 아닌 사람 dfs 함수 호출
for i in range(N):
    for j in range(N):
        if visited[i][j]==0: #방문한 적 없을 때
            dfs(j,i)
            result+=1

#visited 값 재설정
visited = [[0]*N for _ in range(N)]

#'G'를 'R'로 바꿔주기
for i in range(N):
    for j in range(N):
        if graph[i][j]=='G':
            graph[i][j]='R'


# 적록색약 아닌 사람
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            dfs(j,i)
            result2 +=1

print(result,result2)
