n = int(input())
cnt=0
h, m, s = 0,0,0

#시간

for i in range(1,n+1):
    h+=1
    check = list(str(h))

    if '3' in check:
        cnt+=1

cnt*60*60

cnt=0
# 분, 초

for i in range(1,61):
    m += 1
    check = list(str(m))

    if '3' in check:
        cnt += 1

print(cnt)