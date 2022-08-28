import sys
input = sys.stdin.readline

h,w = map(int,input().split())
block_list = list(map(int,input().split()))
ans = 0

for i in range(1,w-1):
    left = max(block_list[:i])
    right = max(block_list[i:])
    compare = min(left,right)
    if block_list[i]<compare:
        ans = ans + compare - block_list[i]

print(ans)