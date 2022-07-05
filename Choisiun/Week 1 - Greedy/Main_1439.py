n = input()

zero, one = 0, 0

# 0이면 트루 1이면 False
if n[0] == '1':
    before = False
    one += 1
else:
    before = True
    zero += 1

for index in range(1, len(n)):

    if before and n[index] == '1':
        one += 1
        before = False
    elif not before and n[index] == '0':
        zero += 1
        before = True

if one > zero:
    ans = zero
else:
    ans = one


print(ans)




