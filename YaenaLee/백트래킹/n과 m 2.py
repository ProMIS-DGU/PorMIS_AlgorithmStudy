import sys
input = sys.stdin.readline
n,m = map(int,input().split())
visited = [0]*(n+1)
ans = [0]*m
def dfs(x):
    if x == m:
        print(*ans)
        return
    for i in range(1,n+1):
        if not visited[i] and ans[x-1]<i:
            ans[x] = i
            visited[i] = 1
            dfs(x+1)
            visited[i] = 0
            ans[x] = 0



dfs(0)