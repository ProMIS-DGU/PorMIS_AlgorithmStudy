n = int(input())

five = n//5
two = (n % 5)//2

while True:
    if five == -1:
        print(-1)
        break

    elif n - (5 * five) - (two * 2) == 0:
        print(five + two)
        break

    else:
        five -= 1
        two = (n - (5 * five)) // 2