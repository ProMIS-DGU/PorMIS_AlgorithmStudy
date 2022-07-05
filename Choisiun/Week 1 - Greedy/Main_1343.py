string = input()

count = 0
ans = ''

def cal(ans, count):
    while count != 0:
        if count >= 4:
            ans += 'AAAA'
            count -= 4
        elif count >= 2:
            ans += 'BB'
            count -= 2
        else:
            break

    return ans, count

for ch in string:
    if ch == 'X':
        count += 1

    elif ch =='.':
        ans, count = cal(ans, count)
        if count == 1:
            ans = '-1'
            break
        count = 0
        ans += '.'

ans, count = cal(ans, count)

print(ans if count == 0 else '-1')

