import sys
input = sys.stdin.readline

# n : 배열의 크기, d: 각도

n , d = map(int, input().split())

test_case= []
result = []
#테스트 케이스 입력
for _ in range(n):
    x = list(map(int,input().split()))
    test_case.append(x)
    result.append(x)

middle = int(((n+1)/2)-1)


if(d>0 and d%45==0):
    for i in range(d//45):
        result[middle][middle] = test_case[middle][middle]

        #주대각선 옮기기
        diff = middle
        for i in range(middle):
            result[i][i + diff] = test_case[i][i]
            diff=diff-1
        i=1
        for j in range(middle+1,n):
            result[j][j-(1*i)] = test_case[j][j]
            i+=1
        #도대체 왜 둘 다 바뀌는 거야...........
        print(result)
        print(test_case)
        #가운데 열
        for i in range(middle):
            print(test_case[i][middle])
            result[i][middle+middle-(1*i)] = test_case[i][middle]
            print(result[i][middle + middle - (1 * i)])
        i = 1
        for j in range(middle+1,n):
            result[j][middle-(1*i)]= test_case[j][middle]
            i+=1

        # 부대각선 옮기기

        for i in range(middle):
            result[middle][n-1-(1*i)] = test_case[i][n-1-(1*i)]

        for j in range(middle):
            result[middle][j] = test_case[n-1-(1*j)][j]

        #가운데 행 옮기기

        for i in range(n):
            result[i][i] = test_case[middle][i]

