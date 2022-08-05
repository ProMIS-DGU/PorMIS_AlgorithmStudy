#문제풀이1
#import sys
#
# n = int(sys.stdin.readline())
# list = []
#
# for _ in range(n):
#     x = sys.stdin.readline().rstrip()
#     list.append(x)
#
# list = sorted(list)
# total_num = len(list)
#
# while len(list) != 0:
#     ratio = round((list.count(list[0]) / total_num)*100, 4)
#     print(list[0], ratio)
#     list = [i for i in list if i not in list[0]]

#문제풀이 2
# import sys
# trees = {} # tree 저장하는 딕셔너리
# n=0 #전체 나무 개수 세기
#
# while True:
#     tree = sys.stdin.readline().rstrip() #나무 이름 받아오기
#     if tree=='': #아무것도 입력되지 않으면 종료
#         break
#     if tree in trees: #dic 안의 tree 키 값이 있으면
#         trees[tree] +=1 # 값 +1해주기
#     else:
#         trees[tree] = 1 #없으면 값은 1
#     n+=1
#
# tree_list = list(trees.keys()) #키값들만 리스트 형태로 변환. 키 값들은 중복되지 않음.
# tree_list.sort() #리스트 정렬
# for tree in tree_list:
#     ratio = round(trees[tree]/n*100, 4)
#     print(tree,ratio)

from collections import defaultdict # defaultdict을 사용하겠다
import sys
trees = defaultdict(int) #디폴트 값이 int인 defaultdict
n=0

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    trees[tree] +=1 #default 값을 지정해주지 않아도 됨. tree값이 없으면 기존의 0값에 1추가, 있으면 그 값에 1추가
    n+=1

tree_list = list(trees.keys()) #키값들만 리스트 형태로 변환. 키 값들은 중복되지 않음.
tree_list.sort() #리스트 정렬
for tree in tree_list:
    ratio = round(trees[tree]/n*100, 4)
    print(tree,'%.4f' %ratio)