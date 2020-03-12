q = int(input())
for _ in range(q):
    n = int(input())
    num = list(map(int, input().split()))

    # 일단 회문인지
    flag = 0
    for i in range(n//2):
        if num[i] != num[n-i-1]:
            flag = 1
            break
    if flag == 0:
        print('YES')
        continue
    elif flag == 1:
        flag2 = 0
        for i in range(n):
            for j in range(i+2,n):
                if num[i] == num[j]:
                    flag2 = 1
                    break
            if flag2 == 1:
                break
        if flag2 == 1:
            print('YES')
        elif flag2 == 0:
            print('NO')