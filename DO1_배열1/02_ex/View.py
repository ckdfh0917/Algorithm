for test_case in range(1, 11):
    # 입력 값 받기
    N = int(input())
    numbers = list(map(int, input().split()))

    # 2차원 배열 생성
    arr = [[0 for _ in range(255)] for _ in range(N)]
    
    x = 0
    #입력 받은 아파트 층 수를 생성한 2차원 배열에 대입  
    for k in numbers:        
        for y in range(k):
            arr[x][y] = 1
        x += 1
        
    # 결과값 초기화
    result = 0
    #print(arr[254][0])
    
    
    # 아래층부터 조망권의 조건이 만족하는 지 찾음
    for x in range(0,N):
        for y in range(0,255):
            if arr[x][y] == 1:
                if arr[x+1][y]==0 and arr[x+2][y]==0 and arr[x-1][y]==0 and arr[x-2][y]==0:
                    result += 1
    # 결과 출력
    print('#{} {}' .format(test_case, result))