r, c, k = map(int, input().split())

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

# 1. R 연산인지 C 연산인지 판별
R = len(arr)
C = len(arr[0])

# 행 연산
if R >= C:
    for i in range(R):
        numbers = {}
        new_arr = []
        # 열의 수의 등장 횟수 세기
        for j in range(C):
            if arr[i][j] in numbers:
                numbers[arr[i][j]] += 1
            else:
                numbers[arr[i][j]] = 1
        # 정렬하기
        new_numbers = sorted(numbers.items(), key=lambda x: (x[1], x[0]))

        # 행에 추가하기
        for j in range(C):
            if j < len(new_numbers):
                new_arr.extend(new_numbers[j])
            else:
                new_arr.extend([0, 0])

        arr[i] = new_arr
# 열 연산
else:
    for j in range(C):
        numbers = {}
        new_arr = []
        # 열의 수의 등장 횟수 세기
        for i in range(R):
            if arr[i][j] in numbers:
                numbers[arr[i][j]] += 1
            else:
                numbers[arr[i][j]] = 1
        # 정렬하기
        new_numbers = sorted(numbers.items(), key=lambda x: (x[1], x[0]))

        # 행에 추가하기
        for j in range(C):
            if j < len(new_numbers):
                new_arr.extend(new_numbers[j])
            else:
                new_arr.extend([0, 0])

print(arr)
