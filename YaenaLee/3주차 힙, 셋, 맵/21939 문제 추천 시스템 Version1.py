# x가 1이면 가장 어려운 문제, 난이도 같으면 숫자 큰 문제
# x가 -1이면 가장 쉬운 문제, 난이도 같으면 숫자 작은 문제
# add P L -> L은 난이도, P는 문제번호
# solved P -> 문제번호 P 삭제
import operator
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
for i in range(n):
    p, l = map(int,input().split())
    dictionary[p] = l


dictionary = dict(sorted(dictionary.items(),key = lambda x:(x[1],x[0])))
# print(dictionary)
m = int(input())
for i in range(m):
    input_list = list(input().strip().split())
    if input_list[0]=="recommend":
        # print(dict2)
        num = int(input_list[1])

        if num == 1:
            dict2 = dict(sorted(dictionary.items(), key=lambda x: (x[1], x[0]),reverse=True))
            print(list(dict2)[0])
        if num == -1:
            print(list(dictionary)[0])

    if input_list[0] == "add":
        dictionary[int(input_list[1])] = int(input_list[2])
        dictionary = dict(sorted(dictionary.items(), key=lambda x: (x[1], x[0])))
        # print(dictionary)
    if input_list[0] == "solved":
        del dictionary[int(input_list[1])]
        # print(dictionary)