import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n, m = map(int,input().split())

cheese = []
for _ in range(n):
    graph = list(map(int, input().split()))
    cheese.append(graph)

visited = [[False]*m for _ in range(n)]

#이동방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#결과
result=0


def dfs(x,y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<nx<m and 0<ny<n and cheese[ny][nx]==0 and visited[ny][nx]==False:
            visited[ny][nx]=True
            dfs(nx,ny)

for i in range(n):
    for j in range(m):
        if cheese[i][j]==0 and visited[i][j]==False:
            visited[i][j]=True
            dfs(j,i)
            result+=1

print(result)