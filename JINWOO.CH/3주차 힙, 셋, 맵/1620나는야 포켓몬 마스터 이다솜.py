import sys

pokemon = {} #딕셔너리
num=1
N, M = map(int, input().split()) # 포켓몬, 맞춰야 하는 문제 갯수


for i in range(N):

    x = sys.stdin.readline().rstrip()
    pokemon[x] = num #포켓몬 이름 : 숫자

    num+=1

list=list(pokemon)

for r in range(M):
    y = sys.stdin.readline().rstrip()

    if (y.isdigit()): #숫자로 바꿀 수 있으면
        print(list[int(y)-1]) #인덱스 번호 출력
    else:
        print(pokemon.get(y)) #값 출력

