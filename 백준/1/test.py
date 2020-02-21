import sys

sys.stdin = open('input.txt', 'r')
switch_num = int(input())
switch = list(map(int, input().split()))

N = int(input())
for i in range(N):
    sex, num = map(int, input().split())  # 남자가 1 여자가 2

    if sex == 1:
        for i in range(num - 1, switch_num, num):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    elif sex == 2:
        # 자기 번호 바꾸기
        if switch[num - 1] == 1:
            switch[num - 1] = 0
        else:
            switch[num - 1] = 1
        # 인접한 번호 바꾸기
        i = 1
        while 0 <= num - i - 1 < switch_num and 0 <= num + i - 1 < switch_num:
            if switch[num - i - 1] == switch[num + i - 1]:
                if switch[num - i - 1] == 1:
                    switch[num - i - 1] = 0
                    switch[num + i - 1] = 0
                elif switch[num - i - 1] == 0:
                    switch[num - i - 1] = 1
                    switch[num + i - 1] = 1
                i += 1
            else:
                break

            if i > (switch_num // 2):
                break
print(switch)
for i in range(switch_num):
    print(switch[i],end=' ')
    if (i+1) % 20 == 0:
        print()