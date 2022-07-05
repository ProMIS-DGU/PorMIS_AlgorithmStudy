n = int(input())
target = int(input())

arr: int = [[0] * n for _ in range(n)]

arr[0][0] = n * n

# 초기 인덱스 세팅
x = 0
y = 0

# 회전을 위한 상태 관리 변수
# state = 0 -> y += 1
# state = 1 -> x += 1
# state = 2 -> y -= 1
# state = 3 -> x -= 1
state = 0

ansy = 0
ansx = 0

moves = [[1, 0], [0, 1], [0, -1], [-1, 0]]

while True:

    state = state % 4

    ny = y + moves[state][0]
    nx = x + moves[state][1]

    if arr[y][x] == target:
        ansy = y
        ansx = x

    if arr[y][x] == 1:
        break

    if ny >= n or nx >= n or nx < 0 or ny < 0:
        state += 1
        continue

    if arr[ny][nx] != 0 :
        state += 1
        continue

    arr[ny][nx] = arr[y][x] - 1

    y = ny
    x = nx

for i in range(n):
    print(*arr[i])

print(ansy+1, ansx+1)
