import sys
input = sys.stdin.readline

n, m = map(int,input().split())
ans = [0]*m
visited = [0]*(n+1)

def dfs(x):
    if x==m:
        print(*ans)
        return

    for i in range(1,n+1):
        if ans[x-1]<=i:
            ans[x] = i

            dfs(x+1)

            ans[x] = 0

dfs(0)