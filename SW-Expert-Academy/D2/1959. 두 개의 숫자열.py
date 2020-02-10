q = int(input())

for test_case in range(1, q + 1):
    N, M = map(int, input().split())    # N : 첫번째 숫자열 길이 M : 두번째 숫자열 길이
    print('#{} '.format(test_case), end='')

    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    # 반복횟수를 위한 N,M 차
    k = abs(N - M)

    sum_list = []
    # N의 문자열이 더 길 떄
    if N >= M:
        for i in range(k + 1):
            temp = []
            for j in range(M):
                temp += [list_a[i + j] * list_b[j]]
            sum_list.append(sum(temp))
        print(max(sum_list))
    # M의 문자열이 더 길 때
    else:
        for i in range(k + 1):
            temp = []
            for j in range(N):
                temp += [list_a[j] * list_b[i + j]]
            sum_list.append(sum(temp))
        print(max(sum_list))