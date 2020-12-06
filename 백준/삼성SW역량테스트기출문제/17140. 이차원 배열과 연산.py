r, c, k = map(int, input().split())

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

cnt = 0
while True:
    # 1. R 연산인지 C 연산인지 판별
    R = len(arr)
    C = len(arr[0])

    # print('rrrrrrrrrrrrr cccccccccccccc', R, C, cnt)
    # 탈출 조건
    if r-1 < R and c-1 < C and arr[r-1][c-1] == k:
        # print('탈출 조건', r-1, c-1, arr[r-1][c-1], k)
        break
    cnt += 1

    if cnt == 101:
        cnt = -1
        break

    # 행 연산
    if R >= C:
        maxV = 0
        temp_arr = []
        for i in range(R):
            numbers = {}
            new_arr = []
            # 열의 수의 등장 횟수 세기
            for j in range(C):
                if j > 100:
                    break
                if arr[i][j] in numbers:
                    numbers[arr[i][j]] += 1
                else:
                    if arr[i][j] == 0:
                        continue
                    numbers[arr[i][j]] = 1
            # 정렬하기
            new_numbers = sorted(numbers.items(), key=lambda x: (x[1], x[0]))

            # 행에 추가하기
            for j in range(C):
                if j < len(new_numbers):
                    new_arr.extend(new_numbers[j])

            maxV = max(maxV, len(new_arr))

            if len(new_arr) > 100:
                temp_arr.append(new_arr[:100])
            else:
                temp_arr.append(new_arr)

        arr = []
        for i in range(len(temp_arr)):
            x = maxV - len(temp_arr[i])
            for _ in range(x):
                temp_arr[i].extend([0])
            arr.append(temp_arr[i])

    # 열 연산
    else:
        rotation_arr = [[0] * R for _ in range(C)]

        # 시계방향으로 arr 회전
        for i in range(R):
            for j in range(C):
                rotation_arr[j][R-1-i] = arr[i][j]

        # print('rotation')
        # print(rotation_arr)
        temp_arr = []
        maxV = 0
        for i in range(C):
            numbers = {}
            new_arr = []
            # 열의 수의 등장 횟수 세기
            for j in range(R):
                if j > 100:
                    break
                if rotation_arr[i][j] in numbers:
                    numbers[rotation_arr[i][j]] += 1
                else:
                    if rotation_arr[i][j] == 0:
                        continue
                    numbers[rotation_arr[i][j]] = 1
            # 정렬하기
            new_numbers = sorted(numbers.items(), key=lambda x: (x[1], x[0]))

            # 행에 추가하기
            for j in range(C):
                if j < len(new_numbers):
                    new_arr.extend(new_numbers[j])
            maxV = max(maxV, len(new_arr))

            new_arr.reverse()
            if len(new_arr) > 100:
                temp_arr.append(new_arr[:100])
            else:
                temp_arr.append(new_arr)


        # 반시계 90도 회전
        arr = [[0] * len(temp_arr) for _ in range(maxV)]
        for i in range(len(temp_arr)):
            for j in range(len(temp_arr[i])):
                arr[len(temp_arr[i])-1-j][i] = temp_arr[i][j]


print(cnt)