#치즈
#치즈를 공중에 놓으면 녹게됨
#공기와 접촉된 칸은 한 시간 지나면 녹아 없어짐
#치즈 구멍 속에는 공기 X , 구멍을 둘러싼 치즈가 녹아 구멍이 열리면 구멍 속으로 공기가 들어감

#요약하자면 공기에 접촉한 칸이 녹는다!
from collections import deque
import sys
input = sys.stdin.readline
h,w = map(int,input().split())
cheeze_list = []


for i in range(h):
    a = list(map(int, input().split()))
    cheeze_list.append(a)

# print(cheeze_list)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = 0

melt = []
while True:
    queue = deque([(0, 0)])
    visited = [[False for i in range(w)] for j in range(h)]
    visited[0][0] = True
    cnt = 0
    # print(queue)
    while queue:
        # print(cheeze_list)
        x,y = queue.popleft()
        # print(x,y)
        if cheeze_list[x][y]==1:
            continue
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x>=h or new_x<0 or new_y>=w or new_y<0:
                continue
            if visited[new_x][new_y]:
                continue
            if cheeze_list[new_x][new_y]==0:
                queue.append((new_x,new_y))
                visited[new_x][new_y] = True
            if cheeze_list[new_x][new_y] == 1:
                cheeze_list[new_x][new_y] = 0
                visited[new_x][new_y] = True
                cnt += 1


    if cnt == 0:
        break
    ans +=1
    melt.append(cnt)
print(ans)
print(melt[-1])