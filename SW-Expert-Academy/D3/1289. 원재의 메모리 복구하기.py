import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q + 1):
    num = input()

    cnt = 0
    temp = num[0]
    flag = 0
    flag2 = 0
    for i in range(1, len(num)):
        if num[0] == '1' and flag2 == 0:
            flag2 = 1
            cnt += 1
        if num[i - 1] != num[i]:
            cnt += 1
            temp = num[i]

    print('#{} {}'.format(test_case, cnt))

## 0에서 1로 바뀐 수와 1에서 0으로 바뀐 수를 센 것이 답