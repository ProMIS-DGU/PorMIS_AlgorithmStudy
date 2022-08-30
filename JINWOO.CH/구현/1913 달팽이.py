n =int(input())
given_number=int(input())
answer=[] # given_number x, y 값

snail = [[0]*(n) for _ in range(n)]
num=1 # 칸 안에 들어가는 숫자

#가운데 1먼저 넣고 시작
x, y = int((n+1)/2)-1,int((n+1)/2)-1
snail[x][y] = num

a=1
b=2

while snail[0][0]!=n*n:
    #위로 한 칸
    x=x-1
    num+=1

    snail[x][y] = num

    for i in range(1,a+1):
        #오른쪽으로
        y=y+1
        num+=1

        snail[x][y] = num

        if(num==given_number):
            answer.append(x)
            answer.append(y)

    for i in range(1,b+1):
        #아래로
        x=x+1
        num+=1
        snail[x][y] = num

        if (num == given_number):
            answer.append(x)
            answer.append(y)

    for i in range(1,b+1):
        #왼쪽
        y=y-1
        num+=1
        snail[x][y] = num

        if (num == given_number):
            answer.append(x)
            answer.append(y)

    for i in range(1,b+1):
        #위로
        x=x-1
        num+=1
        snail[x][y] = num

        if (num == given_number):
            answer.append(x)
            answer.append(y)

    a+=2
    b+=2


for i in range(n):
    print(" ".join(map(str,snail[i])))

print(answer[0]+1,answer[1]+1)