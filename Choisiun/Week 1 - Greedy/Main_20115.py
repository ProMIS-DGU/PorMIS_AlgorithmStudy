import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort(reverse= True)

L = arr[0]
for i in range(1, len(arr)):
    R = arr[i]

    if L < R:
        L = R + L/2
    else:
        L = L + R/2

print(L)
