import sys
input = sys.stdin.readline

n, m = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
ans = [0]*m
visited = [0]*n

def dfs(x):
    if x==m:
        print(*ans)
        return

    for i in range(0,n):
        if not visited[i] :
            ans[x] = num_list[i]
            visited[i] = 1
            dfs(x+1)
            visited[i] = 0
            ans[x]=0

dfs(0)