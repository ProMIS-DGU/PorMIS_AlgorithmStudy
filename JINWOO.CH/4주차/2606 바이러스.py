n = int(input())
m = int(input())


#인접행렬 만들기
# 참고 : https://velog.io/@tks7205/dfs%EC%99%80-bfs%EB%A5%BC-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95-in-python
graph = [[0]*(n+1) for _ in range(n+1)]

# 행렬 안에 주어진 값 넣기
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a] = 1
#방문 표시
visited=[0]*(n+1)

# 함수 정의
result = 0

def dfs(x) :
    visited[x] = 1
    global result #전역변수
    for i in range(1,n+1):
        if graph[x][i] ==1 and visited[i] == 0: #연결되어 있고, 방문 기록이 없으면
            result = result + 1
            dfs(i)
dfs(1)
print(result)