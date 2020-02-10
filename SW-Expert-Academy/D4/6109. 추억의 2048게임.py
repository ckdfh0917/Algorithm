import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def command(con, arr, n):
    if con == 'up':
        for j in range(n):
            k = n
            k = (k ** 2) - 1
            i = 0
            # 탐색하는 위치가 0일 때 앞에서 한칸 땡겨오고 0으로 채우기
            while k > 0:
                if i + 1 < n:
                    if arr[i][j] == 0:
                        arr[i][j] = arr[i + 1][j]
                        arr[i + 1][j] = 0
                k -= 1
                i += 1
                if i > n - 1:
                    i -= n
            # 같은 수 일 때 2배 해주기
            for i in range(n-1):
                if arr[i][j] == arr[i+1][j]:
                    arr[i][j] *= 2
                    arr[i+1][j] = 0
            k = n
            k = (k**2) - 1
            i = 0
            # 탐색하는 위치가 0일 때 앞에서 한칸 땡겨오고 0으로 채우기
            while k > 0:
                if i+1 < n:
                    if arr[i][j] == 0:
                        arr[i][j] = arr[i+1][j]
                        arr[i+1][j] = 0
                k -= 1
                i += 1
                if i > n-1:
                    i -= n

    elif con == 'down':
        for j in range(n):
            k = n
            k = (k ** 2) - 1
            i = 0
            # 탐색하는 위치가 0일 때 앞에서 한칸 땡겨오고 0으로 채우기
            while k > 0:
                if i + 1 < n:
                    if arr[n - i - 1][j] == 0:
                        arr[n - i - 1][j] = arr[n - i - 2][j]
                        arr[n - i - 2][j] = 0
                k -= 1
                i += 1
                if i > n - 1:
                    i -= n
            # 같은 수 일 때 2배 해주기
            for i in range(n-1):
                if arr[n-i-1][j] == arr[n-i-2][j]:
                    arr[n-i-1][j] *= 2
                    arr[n-i-2][j] = 0
            k = n
            k = (k**2) - 1
            i = 0
            # 탐색하는 위치가 0일 때 앞에서 한칸 땡겨오고 0으로 채우기
            while k > 0:
                if i+1 < n:
                    if arr[n-i-1][j] == 0:
                        arr[n-i-1][j] = arr[n-i-2][j]
                        arr[n-i-2][j] = 0
                k -= 1
                i += 1
                if i > n-1:
                    i -= n
    elif con == 'right':
        for i in range(n):
            k = n
            k = (k ** 2) - 1
            j = 0
            # 탐색하는 위치가 0일 때 앞에서 한칸 땡겨오고 0으로 채우기
            while k > 0:
                if n - j - 1 > 0:
                    if arr[i][n - j - 1] == 0:
                        arr[i][n - j - 1] = arr[i][n - j - 2]
                        arr[i][n - j - 2] = 0
                k -= 1
                j += 1
                if j > n - 1:
                    j -= n
            # 같은 수 일 때 2배 해주기
            for j in range(n-1):
                if arr[i][n-j-1] == arr[i][n-j-2]:
                    arr[i][n-j-1] *= 2
                    arr[i][n-j-2] = 0

            k = n
            k = (k**2) - 1
            j = 0
            # 탐색하는 위치가 0일 때 앞에서 한칸 땡겨오고 0으로 채우기
            while k > 0:
                if n-j-1 > 0:
                    if arr[i][n-j-1] == 0:
                        arr[i][n-j-1] = arr[i][n-j-2]
                        arr[i][n-j-2] = 0
                k -= 1
                j += 1
                if j > n-1:
                    j -= n
    elif con == 'left':
        for i in range(n):
            k = n
            k = (k ** 2) - 1
            j = 0
            # 탐색하는 위치가 0일 때 앞에서 한칸 땡겨오고 0으로 채우기
            while k > 0:
                if j + 1 < n:
                    if arr[i][j] == 0:
                        arr[i][j] = arr[i][j + 1]
                        arr[i][j + 1] = 0
                k -= 1
                j += 1
                if j > n - 1:
                    j -= n
            # 같은 수 일 때 2배 해주기
            for j in range(n-1):
                if arr[i][j] == arr[i][j+1]:
                    arr[i][j] *= 2
                    arr[i][j+1] = 0

            k = n
            k = (k**2) - 1
            j = 0
            # 탐색하는 위치가 0일 때 앞에서 한칸 땡겨오고 0으로 채우기
            while k > 0:
                if j+1 < n:
                    if arr[i][j] == 0:
                        arr[i][j] = arr[i][j+1]
                        arr[i][j+1] = 0
                k -= 1
                j += 1
                if j > n-1:
                    j -= n
    return arr

for test_case in range(1,q+1):
    N, com = map(str, input().split())
    print('#{} '.format(test_case))
    n = int(N)
    # arr에 입력 받기
    arr = []
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)

    next = command(com, arr, n)
    # 답 출력
    for i in range(n):
        print(' '.join(map(str, next[i])))

