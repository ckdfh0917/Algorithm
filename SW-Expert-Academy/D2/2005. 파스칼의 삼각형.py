import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q + 1):
    number = int(input())

    print('#{}'.format(test_case))
    result = []
    result.append([1])
    result.append([1, 1])
    if number == 1:
        print('1')
    elif number == 2:
        print('1')
        print('1 1')
    else:
        # print(result)
        for col in range(2, number):
            temp = []
            temp += [1]
            for row in range(1, col):
                hap = result[col - 1][row - 1] + result[col - 1][row]
                temp += [hap]
            temp += [1]
            result.append(temp)


        for i in range(len(result)):
            print(' '.join(map(str, result[i])))

#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0 for _ in range(N+1)] for _ in range(N)]
#     arr[0][0] = 1   # 가장 첫번째 칸은 1로 초기화
#     for i in range(1,N):
#         for j in range(1, i+2):
#             arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#     print('#{}' .format(tc))
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j]:
#                 print(arr[i][j], end=' ')
#             print()



