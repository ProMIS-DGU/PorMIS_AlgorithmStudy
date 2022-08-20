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

            ans[x] = i

            dfs(x+1)

            ans[x] = 0



dfs(0)