def men(stu_num, len_num, switch_list):
    for i in range(stu_num - 1, len_num, stu_num):
        if switch_list[i] == 1:
            switch_list[i] = 0
        else:
            switch_list[i] = 1
    return switch_list

def women(stu_num, len_num, switch_list):
    # 자기 번호 바꾸기
    if switch_list[stu_num - 1] == 1:
        switch_list[stu_num - 1] = 0
    else:
        switch_list[stu_num - 1] = 1
    # 인접한 번호 바꾸기
    i = 1
    while 0 <= stu_num - i - 1 < len_num and 0 <= stu_num + i - 1 < len_num:
        if switch_list[stu_num - i - 1] == switch_list[stu_num + i - 1]:
            if switch_list[stu_num - i - 1] == 1:
                switch_list[stu_num - i - 1] = 0
                switch_list[stu_num + i - 1] = 0
            elif switch_list[stu_num - i - 1] == 0:
                switch_list[stu_num - i - 1] = 1
                switch_list[stu_num + i - 1] = 1
            i += 1
        else:
            break
    return switch_list

switch_num = int(input())
switch = list(map(int, input().split()))

N = int(input())
for i in range(N):
    sex, num = map(int, input().split())  # 남자가 1 여자가 2

    if sex == 1:
        switch = men(num, switch_num, switch)
    elif sex == 2:
        switch = women(num, switch_num, switch)

for i in range(switch_num):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0:
        print()