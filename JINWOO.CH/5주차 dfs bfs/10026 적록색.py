import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
graph = []
for _ in range(N):
    color = list(input().rstrip())
    graph.append(color)

visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
result = 0
result2 = 0


# 적록색약 아닌 사람 dfs 함수 정의
def dfs(x, y,s):
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return False

    if graph[y][x] == s and visited[y][x] == 0:
        visited[y][x] = 1

        dfs(x - 1, y, s)
        dfs(x, y - 1, s)
        dfs(x + 1, y, s)
        dfs(x, y + 1, s)
        return True

    return False

for i in range(N):
    for j in range(N):
        if dfs(j,i,graph[i][j])==True:
            result+=1


# 적록색약인 사람 dfs 함수 정의
def dfs2(x, y, s):

    if graph[y][x]=='G':
        graph[y][x]='R'
        s='R'

    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return False

    if graph[y][x] == s and visited2[y][x] == 0:

        visited2[y][x] = 1

        dfs2(x - 1, y, s)
        dfs2(x, y - 1, s)
        dfs2(x + 1, y, s)
        dfs2(x, y + 1, s)
        return True

    return False

for i in range(N):
    for j in range(N):

        if dfs2(j,i,graph[i][j])==True:
            result2 +=1

print(result,result2)
