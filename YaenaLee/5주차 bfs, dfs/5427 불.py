import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    w, h = map(int, input().strip().split())
    fire_map=[]
    for j in range(h):
         fire_map.append(list(input().strip()))

    while True:
        queue = deque([0,0])
        visited = [[0 for i in range(w)] for j in range(h)]
        visited[0][0] = 1
        while queue:
            x,y = queue.popleft()
            if fire_map[x][y]=="#":
                q