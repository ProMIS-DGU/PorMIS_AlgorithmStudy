# x가 1이면 가장 어려운 문제, 난이도 같으면 숫자 큰 문제
# x가 -1이면 가장 쉬운 문제, 난이도 같으면 숫자 작은 문제
# add P L -> L은 난이도, P는 문제번호
# solved P -> 문제번호 P 삭제

import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
array = []
n = int(input())
for i in range(n):
    p, l = map(int,input().split())
    heapq.heappush(array,(l,p))
array2 = []
for i in range(n):
    heapq.heappush(array2,heapq.heappop(array))

# print(array2)

m = int(input())
for i in range(m):
    input_list = list(input().strip().split())
    if input_list[0] == "recommend":
        num = int(input_list[1])
        if num == 1:
            array = sorted(array2,key=lambda x : (x[0],x[1]),reverse=True)
            print(array[0][1])
        else:
            print(array2[0][1])
    if input_list[0] == "add":
        p = int(input_list[1])
        l = int(input_list[2])
        heapq.heappush(array2, (l, p))
        array2.sort(key=lambda x : (x[0],x[1]))
        # print(array2)
    if input_list[0] == "solved":
        num = int(input_list[1])
        for i in array2:
            if i[1] == num:
                array2.pop(array2.index(i))
                break
        # print(array2)