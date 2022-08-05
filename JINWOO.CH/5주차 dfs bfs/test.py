import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[y][x] = 1
    for i in range(4):
        nowx, nowy = x + dx[i], y + dy[i]
        if 0 <= nowx < n and 0 <= nowy < n and arr[y][x] == arr[nowy][nowx] and visited[nowy][nowx] == 0:
            dfs(nowx, nowy)


n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt1 += 1
            dfs(j, i)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

cnt2 = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt2 += 1
            dfs(j, i)

print(cnt1, cnt2)


import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[y][x] = 1
    for i in range(4):
        nowx, nowy = x + dx[i], y + dy[i]
        if 0 <= nowx < n and 0 <= nowy < n and arr[y][x] == arr[nowy][nowx] and visited[nowy][nowx] == 0:
            dfs(nowx, nowy)


n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt1 += 1
            dfs(j, i)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

cnt2 = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt2 += 1
            dfs(j, i)

print(cnt1, cnt2)
