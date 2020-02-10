# 제일 오른쪽 인덱스에서 왼쪽으로 가장 근접한 인덱스까지의 거리 + 제일 오른쪽 인덱스와 오른쪽 벽과의 거리
'''
1
9 8
7 4 2 0 0 6 0 7 0
'''

q = int(input())




for test_case in range(1, q+1):
    N, M = map(int, input().split())  # N : 가로 M : 세로

    box = list(map(int, input().split()))

    max = 0
    temp = N

    result = []

    #print(box)

    for i in range(M):
        result += [9]
    #print(result)

    for i in range(N):
        for j in range(M):
            if j == box[i]:
                for k in range(j):
                    result[k] -= 1


    max_res = 0
    for i in range(M):
        if result[i] == 9:
            result[i] = 0

        if result[i] > max_res:
            max_res = result[i]

    print(result)
    print(max_res)



# 2차원 배열 입력받기
# 3
# 1 2 3
# 4 5 6
# 7 8 9

'''
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

'''