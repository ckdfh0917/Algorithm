# 디버깅용 시험 제출시 제거
import sys
sys.stdin = open('input.txt','r')            # 표준입력을 콘솔창에서 파일로 변경

q = int(input())

for test_case in range(1,q+1):
    K, N, M = map(int, input().split()) #K : 최대 이동할 수 있는 정류장
                                        #N : 정류장 수
                                        #M : 충전소 수
    # station_list 초기화
    station_list = [0 for _ in range(N+1)]
    # 충전소 위치를 입력받음
    charge_list = list(map(int, input().split()))

    # 입력받은 충전소 위치를 station_list 에 표시
    for i in charge_list:
        station_list[i] = 1

    # 전역변수들
    result = 0
    i = 0
    max_a = 0
    flag = 0

    while True:
        # 최대 이동거리를 temp 로 잠시 저장
        temp = K
        max_a = 0
        for j in range(1,K+1):
            # 끝 정류장에 도착하면 break
            if i+j == N:
                flag = 1
                break
            # 최대 이동거리 안에 충전소가 있는지
            if station_list[i+j] == 1:
                # 최대 이동거리 안에 여러 충전소 중 가장 멀리 있는 충전소 위치
                if i+j > max_a:
                    max_a = i+j
            # 최대 이동거리 안에 충전소가 없을 때 마다 temp 를 -1
            elif station_list[i+j] == 0:
                temp -= 1

            # temp = 0 이면 최대 이동거리 안에 충전소가 없다는 것을 의미하므로
            # flag 표시 후 결과를 0으로 하고 break
            if temp == 0:
                flag = 1
                result = 0
                break
        # while 문 탈출
        if flag == 1:
            break

        i = max_a
        result += 1

    print('#{} {}' .format(test_case,result))