import sys
input = sys.stdin.readline

h, w = map(int,input().split())

block = list((map(int,input().split())))

for i in range(w):
    if block[i]!=0:
        standard = (block[i],i)
        break
num=0

for i in range(w):
    if block[i] > standard[0]:
        if i-standard[1]==1:
            continue
        else :
            for j in range(standard[1],i):
                num = num + (standard[0]-block[j])

            standard=(block[i],i)


second_biggest = 0
second_standard =(0,0)

for i in range(standard[1]+1,w):
    if block[i]>second_biggest:
        second_biggest=block[i]
        second_standard = (second_biggest,i)

for i in range(standard[1]+1,w):
    num = num + (second_standard[0] - block[i])

print(num)