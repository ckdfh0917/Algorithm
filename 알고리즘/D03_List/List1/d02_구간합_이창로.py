# 디버깅용 시험 제출시 제거
import sys
sys.stdin = open('input.txt','r')            # 표준입력을 콘솔창에서 파일로 변경

q = int(input())

for test_case in range(1,q+1):
    N, M = map(int, input().split())    # N : N개의 정수
                                        # M : M개의 부분합
    numbers = list(map(int, input().split()))

    # max, min 초기화
    a_max = 0
    a_min = 0

    # min 값 최초 M개의 합으로 지정
    for i in range(M):
        a_min += numbers[i]

    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += numbers[i+j]
        if temp > a_max:
            a_max = temp
        if temp < a_min:
            a_min = temp


    result = a_max - a_min

    print('#{} {}' .format(test_case, result))