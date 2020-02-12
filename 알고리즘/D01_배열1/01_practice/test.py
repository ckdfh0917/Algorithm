for test_case in range(1, 11):
    # 입력 값 받기
    N = int(input())
    numbers = list(map(int, input().split()))

    # 2차원 배열 생성
    arr = [[0 for _ in range(255)] for _ in range(N)]

    x = 0
    # 생성한 배열에 아파트 층 대입
    for k in numbers:
        # print(k)
        for y in range(k):
            arr[x][y] = 1
        x += 1

    # 결과값 초기화
    result = 0
    # print(arr[10][0])

    # 최대층부터
    for x in range(0, N):
        # print(x)
        for y in range(254, 0, -1):
            # print(y)
            if arr[x][y] == 1:
                # print('c')
                if arr[x + 1][y] == 0 and arr[x + 2][y] == 0 and arr[x - 1][y] == 0 and arr[x - 2][y] == 0:
                    print(x, y)
                    result += 1
            # print('e')
    print(result)