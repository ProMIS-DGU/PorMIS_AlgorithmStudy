import sys
import heapq

N = int(sys.stdin.readline()) #총 받을 값

heap=[]

for i in range(N):
    input = int(sys.stdin.readline()) #입력할 값

    if(input!=0): #input값이 0이 아니면 heap에 추가
        heapq.heappush(heap,(abs(input),input)) #튜플 형태(절대값, input값)로 heap에 추가. Q : 뒤에 거 기준?

    else:
        if(len(heap)!=0): #비어있지 않으면
            print(heap[0][1])#heap의 가장 작은 값인 튜플의 첫번째 인덱스 출력
            heapq.heappop(heap)[1]
        else:
            print(0)


#https://littlefoxdiary.tistory.com/3
