n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

count, ans = 0, 0
for weight in arr:
    count += 1

    if weight * count > ans:
        ans = weight * count

print(ans)


