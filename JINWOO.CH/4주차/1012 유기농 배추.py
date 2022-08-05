# T=int(input())
# M, N, K = map(int, input().split())
#
# graph = [[0]*(N) for _ in range(N)]
#
# visited = [0]*N
#
# def dfs()
#
# for _ in range(T):
#     for _ in range(K) :


result=0

# def dfs(x,y):
#     visited[x][y]=1
#     if graph[x][y+1]==1 and visited[x][y+1]==0:
#         visited[x][y+1]=1
#         dfs(x,y+1)
#     if graph[x][y-1]==1 and visited[x][y-1]==0:
#         visited[x][y - 1] = 1
#         dfs(x, y -1)
#     if graph[x-1][y]==1 and visited[x-1][y]==0:
#         visited[x-1][y] = 1
#         dfs(x-1, y)
#     if graph[x+1][y]==1 and visited[x+1][y]==0:
#         visited[x+1][y] = 1
#         dfs(x+1, y)

import sys
sys.setrecursionlimit(10**6) #dfs 사용할 때 붙여야 함.
input = sys.stdin.readline
T = int(input())

def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return

    if graph[x][y] == 0:
        return


    graph[x][y] = 0 # 탐색한 배추는 0으로 갱신

    # 상하좌우 탐색
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)


for _ in range(T):
    M, N, K = map(int, input().split()) # 가로길이, 세로길이, 배추 수
    graph = [[0] * M for _ in range(N)]

    result = 0 # 지렁이 수

    # 그래프 생성
    for _ in range(K): # 배추 수 만큼 반복
        a,b = map(int,input().split())
        graph[b][a] = 1 # 배추 위치 표기

    # dfs
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: # 배추가 존재하는 경우
                dfs(i,j) # 인접 배추 탐색
                result += 1 # dfs 종료하면 지렁이 수 추가

    print(result)