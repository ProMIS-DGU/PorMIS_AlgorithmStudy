from collections import deque
n, k = map(int,input().split())
num_list = deque([i+1 for i in range(n)])
# print(num_list)
ans = []
cnt = 0
while len(num_list)>0:
    cnt = 0
    for i in range(k-1):
        pop_num = num_list.popleft()
        num_list.append(pop_num)
        cnt +=1
        # print(num_list)
        # print(cnt)
    if cnt == k-1:
        ans_num = num_list.popleft()
        ans.append(str(ans_num))


print("<", end = "")
print(", ".join(ans),end="")
print(">", end= "")
