import sys
sys.stdin = open('input2.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    arr = [list(input()) for _ in range(5)]
    # for row in arr:
    #     print(row)
    # 열 방향으로 읽어오기
    # 0행 0열 -> 1행 0열 -> 2행 0열 ...
    # 0행 1열 -> 1행 1열 -> 2행 1열 ...

    for i in range(15):
        for j in range(5):
            # 접근하려는 열이 접근 가능한지 확인
            if i < len(arr[j]) and j < len(arr):
                print(arr[j][i], end='')