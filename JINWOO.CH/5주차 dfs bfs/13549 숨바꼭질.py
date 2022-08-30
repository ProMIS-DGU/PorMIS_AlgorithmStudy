from collections import deque

N, K = map(int, input().split())
result=0

def bfs(x):

    queue=deque()

    queue.append(x)

    while queue:
        x = queue.popleft()


        if 2*x == K:
            return
        else:
            queue.append(2*x)

        if x-1 == K:
            return
        else:
            queue.append(x-1)
            minus+=1
        if x+1 == K:
            return
        else:
            queue.append(x+1)
            return

bfs(N)