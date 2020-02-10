q = int(input())

for test_case in range(1, q + 1):
    a, b, c = map(int, input().split())

    print('#{} '.format(test_case), end='')
    cnt1 = 0
    cnt2 = 0

    if a == b:
        cnt1 = 1
    elif a == c:
        cnt2 = 1

    if cnt1 == 1:
        print(c)
    elif cnt2 == 1:
        print(b)
    else:
        print(a)