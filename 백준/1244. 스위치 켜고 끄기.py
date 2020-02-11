import sys
sys.stdin = open('input.txt', 'r')

def men(stu_num, len_num, switch_list):

    for i in range(stu_num-1,len_num,stu_num):
        if switch_list[i] == 1:
            switch_list[i] = 0
        else:
            switch_list[i] = 1
    return switch_list

def women(stu_num, len_num, switch_list):
    # 자기 번호 바꾸기
    if switch_list[stu_num-1] == 1:
        switch_list[stu_num-1] = 0
    else:
        switch_list[stu_num-1] = 1
    # 인접한 번호 바꾸기
    i = 1
    while stu_num-i-1 >= 0 and stu_num+i-1 < len_num:
        if switch_list[stu_num-i-1] == switch_list[stu_num+i-1]:
            if switch_list[stu_num-i-1] == 1:
                switch_list[stu_num-i-1] = 0
                switch_list[stu_num+i-1] = 0
            elif switch_list[stu_num-i-1] == 0:
                switch_list[stu_num-i-1] = 1
                switch_list[stu_num+i-1] = 1
        else:
            break
        i += 1
    return switch_list

switch_num = int(input())
switch = list(map(int,input().split()))

N = int(input())
print('a [1', end='')
for i in range(2,switch_num+1):
    print(',',i, end='')
print(']')
print('f',switch)
for i in range(N):
    sex, num = map(int, input().split())    # 남자가 1 여자가 2

    if sex == 1:
        switch = men(num, switch_num, switch)
        print('m',switch)
    elif sex == 2:
        switch = women(num, switch_num, switch)
        print('w',switch)

if 0 <= switch_num < 20:
    print(' '.join(map(str, switch[:20])))
elif 20 <= switch_num < 40:
    print(' '.join(map(str, switch[:20])))
    print(' '.join(map(str, switch[20:40])))
elif 40 <= switch_num < 60:
    print(' '.join(map(str, switch[:20])))
    print(' '.join(map(str, switch[20:40])))
    print(' '.join(map(str, switch[40:60])))
elif 60 <= switch_num < 80:
    print(' '.join(map(str, switch[:20])))
    print(' '.join(map(str, switch[20:40])))
    print(' '.join(map(str, switch[40:60])))
    print(' '.join(map(str, switch[60:80])))
elif 80 <= switch_num < 100:
    print(' '.join(map(str, switch[:20])))
    print(' '.join(map(str, switch[20:40])))
    print(' '.join(map(str, switch[40:60])))
    print(' '.join(map(str, switch[60:80])))
    print(' '.join(map(str, switch[80:100])))